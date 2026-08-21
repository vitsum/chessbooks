#!/usr/bin/env python3
"""
Сборка интерактивных приложений по шахматным книгам.

    python3 run.py gen   <book>   — собрать data/data_<book>.json из src/_body_<book>.py
    python3 run.py eval  <book>   — прогнать Stockfish, записать data/cp_<book>.json
    python3 run.py build          — собрать dist/index.html (всё вшито, интернет не нужен)
    python3 run.py check [<book>] — автопроверка на просмотры по оценкам движка
    python3 run.py all   <book>   — gen + eval + gen + build

<book> ∈ alekhine | pirc | kid | grob | bloodgood  (или "all" для gen/eval/check)

Сборка всегда одна: все книги уезжают в dist/index.html, переключаются вкладками.
"""
import sys, os, json, base64, time
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DATA, DIST, VEND = (os.path.join(ROOT, d) for d in ("src", "data", "dist", "vendor"))
sys.path.insert(0, SRC)
from books import BOOKS, META_KEYS, OUT, TITLE

STOCKFISH = os.environ.get("STOCKFISH", "/usr/games/stockfish")
data_path = lambda b: os.path.join(DATA, f"data_{b}.json")
cp_path   = lambda b: os.path.join(DATA, f"cp_{b}.json")
read      = lambda p: open(p, encoding="utf-8").read()


def gen(book):
    """Склеиваем _head + _body_<book> + _tail и исполняем: получаем data_<book>.json."""
    parts = [read(os.path.join(SRC, n))
             for n in ("_head.py", f"_body_{book}.py", "_tail_clean.py")]
    ns = {"DATA_OUT": data_path(book), "CP_IN": cp_path(book),
          "SIDE": BOOKS[book]["side"], "__name__": "__gen__"}
    os.chdir(SRC)                      # чтобы работал `import scan`
    exec(compile("\n".join(parts), f"gen_{book}", "exec"), ns)
    os.chdir(ROOT)


def evaluate(book, depth=16, tmax=0.9):
    """Stockfish по всем позициям всех вариантов -> cp_<book>.json"""
    import chess, chess.engine
    V = json.load(open(data_path(book), encoding="utf-8"))
    eng = chess.engine.SimpleEngine.popen_uci(STOCKFISH)
    eng.configure({"Hash": 128})
    lim = chess.engine.Limit(depth=depth, time=tmax)
    t0, out = time.time(), {}
    for v in V:
        b = chess.Board()
        cps = [eng.analyse(b, lim)["score"].white().score(mate_score=10000)]
        for san in v["moves"]:
            b.push_san(san)
            cps.append(eng.analyse(b, lim)["score"].white().score(mate_score=10000))
        out[v["id"]] = cps
        print(f"  {v['id']:14} {len(cps):3} поз.  [{time.time()-t0:.0f}s]", flush=True)
    eng.quit()
    json.dump(out, open(cp_path(book), "w", encoding="utf-8"))
    print("готово:", sum(len(x) for x in out.values()), "позиций за", round(time.time()-t0), "с")


def _assets(html):
    """Вшиваем библиотеки, css и фигуры."""
    lib = lambda n: read(os.path.join(VEND, n))
    for token, val in [("__JQUERY__", lib("jquery.min.js")),
                       ("__CHESSJS__", lib("chess.cjs.js")),
                       ("__CBJS__", lib("chessboard-1.0.0.min.js")),
                       ("__CBCSS__", lib("chessboard-1.0.0.min.css"))]:
        assert token in html, token
        html = html.replace(token, val)

    pieces = {}
    for f in sorted(os.listdir(os.path.join(VEND, "pieces"))):
        if f.endswith(".svg"):
            raw = open(os.path.join(VEND, "pieces", f), "rb").read()
            pieces[f[:-4]] = "data:image/svg+xml;base64," + base64.b64encode(raw).decode()
    return html.replace("__PIECES__", json.dumps(pieces))


def build(*_):
    """Шаблон + библиотеки + данные всех книг -> один самодостаточный dist/index.html."""
    html = _assets(read(os.path.join(SRC, "template.html")))

    payload = [dict(id=b, **{k: meta[k] for k in META_KEYS},
                    vars=json.load(open(data_path(b), encoding="utf-8")))
               for b, meta in BOOKS.items()]

    for token, val in [("__TITLE__", TITLE),
                       ("__BOOKS__", json.dumps(payload, ensure_ascii=False))]:
        assert token in html, token
        html = html.replace(token, val)

    os.makedirs(DIST, exist_ok=True)
    # newline="\n": иначе на Windows в файл уезжают CRLF и каждая сборка выглядит как правка
    open(os.path.join(DIST, OUT), "w", encoding="utf-8", newline="\n").write(html)

    nv = sum(len(p["vars"]) for p in payload)
    nm = sum(len(v["moves"]) for p in payload for v in p["vars"])
    nn = sum(len(v["notes"]) for p in payload for v in p["vars"])
    print(f"{OUT}: {round(len(html)/1024)} KB, книг {len(payload)}, вариантов {nv}, "
          f"ходов {nm}, комментариев {nn}")


def check(books=None):
    """Ищем ходы, после которых оценка резко падает — признак ошибки в записи."""
    for book in (books or BOOKS):
        if not os.path.exists(data_path(book)): continue
        print(f"=== {book} ===")
        flags = 0
        for v in json.load(open(data_path(book), encoding="utf-8")):
            cp = v.get("cp")
            if not cp: continue
            for i in range(1, len(cp)):
                white = i % 2 == 1
                loss = (cp[i-1]-cp[i]) if white else (cp[i]-cp[i-1])
                if loss > 160:
                    san, note = v["moves"][i-1], v["notes"].get(str(i), "")
                    if "?" in san or "?" in note or "?" in v["title"]: continue
                    flags += 1
                    print(f"  [{v['id']:12}] {(i+1)//2}{'.' if white else '…'}{san:6} "
                          f"{cp[i-1]:>6} → {cp[i]:>6}  (потеря {loss})")
        print(f"  подозрительных ходов: {flags}\n")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    arg = sys.argv[2] if len(sys.argv) > 2 else "all"
    targets = list(BOOKS) if arg == "all" else [arg]
    if arg != "all" and arg not in BOOKS and cmd != "build":
        sys.exit(f"неизвестная книга: {arg}; есть {', '.join(BOOKS)}")
    if cmd == "gen":     [gen(b) for b in targets]
    elif cmd == "eval":  [evaluate(b) for b in targets]
    elif cmd == "build": build()
    elif cmd == "check": check(None if arg == "all" else targets)
    elif cmd == "all":
        for b in targets: gen(b); evaluate(b); gen(b)
        build()
    else: print(__doc__)
