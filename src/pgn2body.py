# -*- coding: utf-8 -*-
"""PGN-книга -> src/_body_<id>.py

Книга Бладгуда пришла не сканом, а базой партий: каждая запись PGN — это вариант
с авторскими комментариями, вложенными вариациями и знаками (!, ?, !?).
Разбирать её глазами незачем, поэтому body-файл собирается отсюда:

    python3 src/pgn2body.py "путь/Tactical Grob.pgn" > src/_body_bloodgood.py

Берутся только теоретические записи (у них в теге White стоит `Variation ...`,
либо `?` — продолжение предыдущей). Партии целиком (записи 41+) пропускаются:
их две с лишним сотни, для репертуара они не нужны.
"""
import io, json, re, sys
import chess, chess.pgn

# NAG -> знак после хода и оценка позиции
GLYPH = {1: "!", 2: "?", 3: "!!", 4: "??", 5: "!?", 6: "?!"}
EVAL = {10: "=", 13: "÷", 14: "²", 15: "³", 16: "±", 17: "∓", 18: "+−", 19: "−+"}

# английские названия разделов -> главы приложения
PARTS = {
    "Part 1: Gambit Accepted":            "Часть 1. Гамбит принят: 2…Bxg4 3.c4",
    "Part 2: Long Diagonal Reinfoced":    "Часть 2. Большая диагональ: 3.c4 dxc4 4.b3",
    "Part 3 (The Open Defense)":          "Часть 3. Открытая защита",
    "Part 4 (Other lines after 1... d5)": "Часть 4. Прочее после 1…d5",
    "Part 5: (1... e5)":                  "Часть 5. 1…e5",
    "Part 6 (1...e5 2.d3)":               "Часть 6. 1…e5 2.d3",
    "Part 7 (1... Various)":              "Часть 7. Разное",
}

SUB_PLIES = 10          # сколько полуходов побочной линии проигрывать на доске
DEEP_PLIES = 120        # предел на текстовую расшифровку вложенной вариации
MAX_DEPTH = 3           # глубже вложенные скобки читать невозможно

# хвост вида «1-0 Bloodgood,C-Clark,J/corr Zugzwang 1975 (23)» — это ссылка на партию,
# а не анализ: показываем её приглушённо, чтобы не мешала читать ходы
import re as _re
CITE = _re.compile(r"^((?:1-0|0-1|1/2-1/2|½-½)\s.*|.*?/(?:corr|[A-Z][a-z]+).*\(\d+\).*)$")


def clean(text):
    """Комментарий PGN -> одна строка."""
    t = " ".join(text.split())
    t = t.replace("$", "").strip()
    return t


def title_of(raw):
    """`Variation \\"A\\" (3...c6 4. cxd5!)` -> `Вариант A · 3…c6 4.cxd5!`"""
    t = raw.replace('\\"', '"').strip()
    m = re.match(r'Variation\s+"?([A-Za-z0-9]+)"?\s*(?:\((.*)\))?\s*$', t)
    if not m:
        return t
    name, tail = m.group(1), (m.group(2) or "").strip()
    tail = re.sub(r"(\d+)\.\s*\.\.\.\s*", r"\1…", tail)
    tail = re.sub(r"(\d+)\s*\.\.\.\s*", r"\1…", tail)
    tail = re.sub(r"(\d+)\.\s+", r"\1.", tail)
    return f"Вариант {name}" + (f" · {tail}" if tail else "")


def slug(name, used):
    s = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower() or "var"
    base, k = s, 2
    while s in used:
        s = f"{base}_{k}"; k += 1
    used.add(s)
    return s


def label(board, move):
    """Ключ комментария ровно в том виде, в каком его печатает _head.build()."""
    n, white = board.fullmove_number, board.turn == chess.WHITE
    san = board.san(move)
    return (f"{n}.{san}" if white else f"{n}...{san}"), san


def line_sans(node, limit):
    """SAN побочной линии от её начала."""
    out, b = [], node.parent.board()
    while node is not None and len(out) < limit:
        out.append(b.san(node.move)); b.push(node.move)
        node = node.variations[0] if node.variations else None
    return out


def glyphs(node):
    return "".join(GLYPH[n] for n in sorted(node.nags) if n in GLYPH)


def say(text):
    """Прозаический кусок: ссылку на партию гасим."""
    t = clean(text)
    return f"<i>{t}</i>" if t and CITE.match(t) else t


def render(node, limit=DEEP_PLIES, top=True, depth=0):
    """Вариация со всеми вложениями -> текст, как в книге:
    `4.Qb3 Qc7 5.cxd5 cxd5 (5…e6 6.h3! Bf5 7.e4) 6.Nc3 and now:`

    Комментарии внутри вариаций — это и есть основной разбор Бладгуда, на главной
    линии их всего 97 из 577. Поэтому вариации расшифровываются целиком, а не
    выбрасываются; scan.py потом сам сделает ходы в этом тексте кликабельными."""
    out, b, k = [], node.parent.board(), 0
    while node is not None and k < limit:
        white = b.turn == chess.WHITE
        san = b.san(node.move)
        num = f"{b.fullmove_number}." if white else (f"{b.fullmove_number}…" if k == 0 and top else "")
        out.append(num + san + glyphs(node))
        if clean(node.comment):
            out.append(say(node.comment))
        b.push(node.move)
        kids = node.variations
        if depth < MAX_DEPTH:
            for alt in kids[1:]:
                inner = render(alt, limit=DEEP_PLIES, top=True, depth=depth + 1)
                if inner:
                    out.append("(" + inner + ")")
        node = kids[0] if kids else None
        k += 1
    return " ".join(out)


def block(alt, board):
    """Альтернатива отдельным блоком: первый ход заголовком, дальше — разбор."""
    white = board.turn == chess.WHITE
    head = (f"{board.fullmove_number}." if white else f"{board.fullmove_number}…") \
        + board.san(alt.move) + glyphs(alt)
    tail = render(alt, top=False, depth=1)
    tail = tail[len(board.san(alt.move) + glyphs(alt)):].strip()
    return f'<div class="alt"><b>{head}</b>{tail}</div>'


def convert(path):
    f = io.open(path, encoding="utf-8", errors="replace")
    games, part, pending = [], None, None
    while True:
        g = chess.pgn.read_game(f)
        if g is None:
            break
        w = g.headers.get("White", "?").replace('\\"', '"')
        if "Variation" not in w and w != "?":
            break                                   # дальше пошли партии целиком
        b = g.headers.get("Black", "?")
        if b in PARTS:
            part = PARTS[b]
        if not g.variations:                        # запись-заголовок без ходов
            pending = title_of(w)
            continue
        name = pending if w == "?" and pending else title_of(w)
        pending = None
        games.append((name, part, g))
    return games


def emit(games):
    used, chapters, out = set(), {}, []
    for name, part, g in games:
        chapters.setdefault(part, len(chapters))

    out.append("# Сгенерировано src/pgn2body.py из «The Tactical Grob» (PGN).")
    out.append("# Комментарии — авторские, на английском: это прямая речь Бладгуда и Гроба.")
    out.append("")
    for ch, i in chapters.items():
        out.append(f'C{i+1} = {json.dumps(ch, ensure_ascii=False)}')
    out.append("")

    subs_all = {}
    for name, part, g in games:
        vid = slug(name, used)
        board = g.board()
        node, moves, notes, subs = g, [], {}, {}
        root = clean(g.comment)

        while node.variations:
            nxt = node.variations[0]
            key, san = label(board, nxt.move)

            # знаки к ходу и авторский текст
            bits = []
            glyph = glyphs(nxt)
            if glyph:
                bits.append(f"<b>{san}{glyph}</b>")
            if root and not moves:
                bits.append(root); root = ""
            if clean(nxt.comment):
                bits.append(clean(nxt.comment))

            # альтернативы этому ходу — каждая своим блоком, с собственным разбором
            alts, blocks = [], []
            for alt in node.variations[1:]:
                sans = line_sans(alt, SUB_PLIES)
                if sans:
                    alts.append((f"вместо {san}", " ".join(sans), "before"))
                blocks.append(block(alt, board))
            if blocks:
                bits.append(f'<div class="alts"><span class="cap">вместо {san}</span>'
                            + "".join(blocks) + "</div>")
            if alts:
                subs[key] = alts

            if bits:
                notes[key] = " — ".join(bits) if len(bits) > 1 else bits[0]

            moves.append(san); board.push(nxt.move); node = nxt

        if not moves:
            continue
        tag = "÷"
        for n in sorted(node.nags):
            if n in EVAL:
                tag = EVAL[n]

        subs_all[vid] = subs
        j = lambda x: json.dumps(x, ensure_ascii=False)
        out.append(f'add({j(vid)}, C{chapters[part]+1}, {j(name)}, {j(tag)}, '
                   f'{j(tag + " по Бладгуду")},')
        out.append(f' {j(" ".join(moves))},')
        if notes:
            items = [f'  {j(k)}: {j(v)}' for k, v in notes.items()]
            out.append(" {\n" + ",\n".join(items) + "})")
        else:
            out.append(" {})")
        out.append("")

    subs_all = {k: v for k, v in subs_all.items() if v}
    out.append("SUBS = " + json.dumps(subs_all, ensure_ascii=False, indent=1)
               .replace("[\n", "[").replace("\n ]", "]"))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "Tactical Grob.pgn"
    sys.stdout.reconfigure(encoding="utf-8", newline="\n")
    print(emit(convert(src)), end="")
