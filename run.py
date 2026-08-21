#!/usr/bin/env python3
"""
Сборка интерактивных приложений по шахматным книгам.

    python3 run.py gen   <book>   — собрать data/data_<book>.json из src/_body_<book>.py
    python3 run.py eval  <book>   — прогнать Stockfish по главным линиям -> data/cp_<book>.json
    python3 run.py subs  <book>   — то же для побочных линий -> data/cpsub_<book>.json
    python3 run.py build          — собрать dist/index.html (всё вшито, интернет не нужен)
    python3 run.py check [<book>] — автопроверка на просмотры по оценкам движка
    python3 run.py cache [<book>] — что уже в кэше оценок и сколько считать (движок не нужен)
    python3 run.py seed  [<book>] — сложить в кэш оценки из cp_*.json и cpsub_*.json
    python3 run.py all   <book>   — gen + eval + gen + subs + gen + build

<book> ∈ alekhine | pirc | kid | grob | bloodgood  (или "all" для gen/eval/check/cache/seed)

Сборка всегда одна: все книги уезжают в dist/index.html, переключаются вкладками.

Оценки движка кэшируются в data/evalcache.json по позиции, и кэш лежит в репозитории.
Поэтому eval/subs/all можно звать сколько угодно: Stockfish поднимается, только если
нашлись позиции, которых в кэше ещё нет. Сколько их — покажет `run.py cache`.
"""
import sys, os, json, base64, time
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DATA, DIST, VEND = (os.path.join(ROOT, d) for d in ("src", "data", "dist", "vendor"))
sys.path.insert(0, SRC)
from books import BOOKS, META_KEYS, OUT, TITLE

STOCKFISH = os.environ.get("STOCKFISH", "/usr/games/stockfish")
data_path = lambda b: os.path.join(DATA, f"data_{b}.json")
cp_path   = lambda b: os.path.join(DATA, f"cp_{b}.json")
sub_path  = lambda b: os.path.join(DATA, f"cpsub_{b}.json")
fen_key   = lambda f: " ".join(f.split()[:4])
read      = lambda p: open(p, encoding="utf-8").read()
CACHE     = os.path.join(DATA, "evalcache.json")


class Evals:
    """Оценки позиций с кэшем на диске.

    Ключ — FEN без счётчиков ходов, так что позиция считается один раз: и когда она
    встречается сразу в десятке вариантов (начало-то у всех общее), и когда те же
    книги пересобирают через полгода. Кэш лежит рядом с данными и коммитится, так что
    движок нужен только под новые позиции, а полная пересборка всех книг без единого
    запуска Stockfish — обычное дело.

    Настройки движка входят в имя раздела кэша: оценки разной глубины перемешивать
    нельзя, но и выбрасывать посчитанное при смене глубины незачем.
    """

    def __init__(self, depth=16, tmax=0.9):
        self.depth, self.tmax = depth, tmax
        self.all = self._load()
        self.pos = self.all.setdefault(f"d{depth}t{tmax}", {})
        self.eng = None
        self.new = self.hit = 0
        self.t0 = time.time()

    @staticmethod
    def _load():
        if not os.path.exists(CACHE):
            return {}
        try:
            return json.load(open(CACHE, encoding="utf-8"))
        except (ValueError, OSError) as e:
            print(f"кэш оценок не читается ({e}) — начинаем новый")
            return {}

    def save(self):
        """Пишем через временный файл: обрыв на середине не должен убить кэш."""
        tmp = CACHE + ".tmp"
        with open(tmp, "w", encoding="utf-8", newline="\n") as f:
            json.dump(self.all, f, separators=(",", ":"), sort_keys=True)
        os.replace(tmp, CACHE)

    def has(self, fen):
        return fen_key(fen) in self.pos

    def score(self, board):
        return self.score_fen(board.fen(), board)

    def score_fen(self, fen, board=None):
        """Оценка позиции: из кэша, а если её там нет — от движка."""
        k = fen_key(fen)
        if k in self.pos:
            self.hit += 1
            return self.pos[k]
        import chess, chess.engine
        if self.eng is None:            # движок поднимаем только ради новых позиций
            print(f"  поднимаю Stockfish ({STOCKFISH})", flush=True)
            self.eng = chess.engine.SimpleEngine.popen_uci(STOCKFISH)
            self.eng.configure({"Hash": 128})
        lim = chess.engine.Limit(depth=self.depth, time=self.tmax)
        board = board if board is not None else chess.Board(fen)
        self.pos[k] = self.eng.analyse(board, lim)["score"].white().score(mate_score=10000)
        self.new += 1
        if self.new % 50 == 0:          # чтобы обрыв не съел час счёта
            self.save()
            print(f"  новых позиций {self.new} [{time.time()-self.t0:.0f}s]", flush=True)
        return self.pos[k]

    def close(self):
        if self.eng:
            self.eng.quit()
            self.eng = None
        self.save()
        print(f"кэш: взято готовых {self.hit}, посчитано {self.new}, "
              f"всего в кэше {len(self.pos)} позиций")


def gen(book):
    """Склеиваем _head + _body_<book> + _tail и исполняем: получаем data_<book>.json."""
    parts = [read(os.path.join(SRC, n))
             for n in ("_head.py", f"_body_{book}.py", "_tail_clean.py")]
    ns = {"DATA_OUT": data_path(book), "CP_IN": cp_path(book), "CPSUB_IN": sub_path(book),
          "SIDE": BOOKS[book]["side"], "__name__": "__gen__"}
    os.chdir(SRC)                      # чтобы работал `import scan`
    exec(compile("\n".join(parts), f"gen_{book}", "exec"), ns)
    os.chdir(ROOT)


def evaluate(book, ev=None):
    """Главные линии -> cp_<book>.json: оценка на каждый полуход варианта."""
    import chess
    own, ev = ev is None, ev or Evals()
    V = json.load(open(data_path(book), encoding="utf-8"))
    out, t0 = {}, time.time()
    for v in V:
        b = chess.Board()
        cps = [ev.score(b)]
        for san in v["moves"]:
            b.push_san(san)
            cps.append(ev.score(b))
        out[v["id"]] = cps
    json.dump(out, open(cp_path(book), "w", encoding="utf-8"))
    print(f"{book}: главных линий {len(out)}, "
          f"позиций {sum(len(x) for x in out.values())} [{time.time()-t0:.0f}s]", flush=True)
    if own: ev.close()


def main_positions(book):
    """Позиции главных линий: FEN без счётчиков -> полный FEN."""
    import chess
    V = json.load(open(data_path(book), encoding="utf-8"))
    out = {}
    for v in V:
        b = chess.Board(); out[fen_key(b.fen())] = b.fen()
        for san in v["moves"]:
            b.push_san(san); out[fen_key(b.fen())] = b.fen()
    return out


def sub_positions(book):
    """То же для побочных линий. В данных лежат ходы, доску отматываем сами."""
    import chess
    V = json.load(open(data_path(book), encoding="utf-8"))
    want = {}
    for v in V:
        b = chess.Board(); fens = [b.fen()]
        for san in v["moves"]:
            b.push_san(san); fens.append(b.fen())
        for ply, lst in v.get("subs", {}).items():
            want[fen_key(fens[int(ply)])] = fens[int(ply)]
            for sv in lst:
                for p in sv["plies"]:
                    want[fen_key(p["fen"])] = p["fen"]
        for d in v.get("isubs", {}).values():
            want[fen_key(d["startFen"])] = d["startFen"]
            for p in d["plies"]:
                want[fen_key(p["fen"])] = p["fen"]
    return {k: f for k, f in want.items() if f}


def evaluate_subs(book, ev=None):
    """Побочные линии тоже заслуживают градусника.

    Главные линии считаются по индексу хода, а побочные ветвятся, поэтому
    здесь ключ — FEN без счётчиков: заодно позиции, встречающиеся в разных
    линиях, считаются один раз.
    """
    own, ev = ev is None, ev or Evals()
    want = sub_positions(book)

    t0 = time.time()
    todo = sum(1 for f in want.values() if not ev.has(f))
    print(f"{book}: побочных позиций {len(want)}, из них новых для движка {todo}", flush=True)
    # файл рядом с данными — это результат, а не кэш: убрали линию из книги — ушла и оценка
    out = {k: ev.score_fen(f) for k, f in want.items()}
    json.dump(out, open(sub_path(book), "w", encoding="utf-8"))
    print(f"{book}: записано {len(out)} оценок [{time.time()-t0:.0f}s]", flush=True)
    if own: ev.close()


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


def cache_seed(books=None):
    """Наполнить кэш тем, что уже посчитано в cp_*.json и cpsub_*.json.

    Оценки считали до того, как появился кэш, и терять их поэтому глупо: часы работы
    движка лежат в репозитории готовыми. Здесь они раскладываются по позициям. Заодно
    это способ восстановить кэш, если файл потеряется: данные книг и оценки к ним
    лежат рядом, движок не нужен.

    Одна позиция приходит из разных вариантов с разными оценками: лимит был 0.9 с,
    и от запуска к запуску движок доходил до разной глубины (у начальной позиции
    набралось три десятка значений в пределах трети пешки). Берём медиану — она
    ближе к тому, что движок считает на самом деле, чем случайная из списка.
    """
    import chess, statistics
    ev = Evals()
    было, seen = len(ev.pos), {}
    for book in (books or BOOKS):
        if not os.path.exists(data_path(book)):
            continue
        n = 0
        # главные линии: оценки лежат списком по номеру полухода, доску отматываем сами
        if os.path.exists(cp_path(book)):
            CP = json.load(open(cp_path(book), encoding="utf-8"))
            for v in json.load(open(data_path(book), encoding="utf-8")):
                cps = CP.get(v["id"])
                # длина обязана сойтись с ходами, иначе оценки лягут не на свои позиции
                if not cps or len(cps) != len(v["moves"]) + 1:
                    if cps: print(f"    пропуск {v['id']}: оценки не сходятся с ходами")
                    continue
                b = chess.Board()
                fens = [b.fen()]
                for san in v["moves"]:
                    b.push_san(san); fens.append(b.fen())
                for f, cp in zip(fens, cps):
                    if cp is not None:
                        seen.setdefault(fen_key(f), []).append(cp); n += 1
        # побочные: там уже ключ по позиции
        if os.path.exists(sub_path(book)):
            for k, cp in json.load(open(sub_path(book), encoding="utf-8")).items():
                if cp is not None:
                    seen.setdefault(k, []).append(cp); n += 1
        print(f"  {book:10} из книги {n:6} оценок")

    spread = 0
    for k, vals in seen.items():
        if k in ev.pos:                 # посчитанное движком уже точнее, не трогаем
            continue
        if max(vals) != min(vals):
            spread += 1
        ev.pos[k] = int(statistics.median_low(vals))
    ev.save()
    print(f"кэш: было {было}, стало {len(ev.pos)} позиций; "
          f"у {spread} из них оценки в книгах расходились, взята медиана")


def cache_stats(books=None):
    """Что уже посчитано и сколько движку осталось. Сам движок не поднимаем:
    это ответ на вопрос «а не встанет ли сборка на час», а не сама сборка."""
    ev = Evals()
    print(f"кэш {os.path.relpath(CACHE, ROOT)}: {len(ev.pos)} позиций, глубина {ev.depth}\n")
    todo = set()
    for book in (books or BOOKS):
        if not os.path.exists(data_path(book)):
            continue
        main, subs = main_positions(book), sub_positions(book)
        both = dict(main, **subs)
        new = {k for k in both if k not in ev.pos}
        todo |= new
        print(f"  {book:10} главных {len(main):5}, побочных {len(subs):6}, "
              f"своих позиций {len(both):6}, новых {len(new):6}")
    if todo:
        print(f"\nсчитать движком: {len(todo)} позиций, это примерно "
              f"{len(todo) * 0.9 / 60:.0f} мин (по 0.9 с на позицию)")
    else:
        print("\nвсё посчитано, движок не нужен")


def check(books=None):
    """Ищем ходы, после которых оценка резко падает — признак ошибки в записи."""
    for book in (books or BOOKS):
        if not os.path.exists(data_path(book)): continue
        print(f"=== {book} ===")
        flags = 0
        for v in json.load(open(data_path(book), encoding="utf-8")):
            cp = v.get("cp")
            if not cp: continue
            # первый ход пропускаем: это выбор дебюта, а не ошибка записи.
            # Stockfish считает 1.g4 примерно на −1.3 за белых — так и есть,
            # но книга про Гроб именно про это, флагом тут делу не поможешь.
            for i in range(2, len(cp)):
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
    elif cmd == "eval":  ev = Evals(); [evaluate(b, ev) for b in targets]; ev.close()
    elif cmd == "subs":  ev = Evals(); [evaluate_subs(b, ev) for b in targets]; ev.close()
    elif cmd == "build": build()
    elif cmd == "check": check(None if arg == "all" else targets)
    elif cmd == "cache": cache_stats(None if arg == "all" else targets)
    elif cmd == "seed":  cache_seed(None if arg == "all" else targets)
    elif cmd == "all":
        # кэш один на весь прогон: книги делят между собой и начала линий, и перестановки
        ev = Evals()
        for b in targets: gen(b); evaluate(b, ev); gen(b); evaluate_subs(b, ev); gen(b)
        ev.close()
        build()
    else: print(__doc__)
