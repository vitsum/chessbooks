#!/usr/bin/env python3
"""
Сборка интерактивных приложений по шахматным книгам.

    python3 run.py gen   <book>   — собрать data/data_<book>.json из src/_body_<book>.py
    python3 run.py eval  <book>   — прогнать Stockfish, записать data/cp_<book>.json
    python3 run.py build <book>   — собрать dist/<...>.html (всё вшито, интернет не нужен)
    python3 run.py check [<book>] — автопроверка на просмотры по оценкам движка
    python3 run.py all   <book>   — gen + eval + gen + build

<book> ∈ alekhine | pirc | kid  (или "all" для build/gen)
"""
import sys, os, json, base64, subprocess, time
ROOT = os.path.dirname(os.path.abspath(__file__))
SRC, DATA, DIST, VEND = (os.path.join(ROOT, d) for d in ("src", "data", "dist", "vendor"))
sys.path.insert(0, SRC)
from books import BOOKS

STOCKFISH = os.environ.get("STOCKFISH", "/usr/games/stockfish")
data_path = lambda b: os.path.join(DATA, f"data_{b}.json")
cp_path   = lambda b: os.path.join(DATA, f"cp_{b}.json")


def gen(book):
    """Склеиваем _head + _body_<book> + _tail и исполняем: получаем data_<book>.json."""
    parts = [open(os.path.join(SRC, n), encoding="utf-8").read()
             for n in ("_head.py", f"_body_{book}.py", "_tail_clean.py")]
    ns = {"DATA_OUT": data_path(book), "CP_IN": cp_path(book), "__name__": "__gen__"}
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
    json.dump(out, open(cp_path(book), "w"))
    print("готово:", sum(len(x) for x in out.values()), "позиций за", round(time.time()-t0), "с")


def build(book):
    """Шаблон + библиотеки + фигуры + данные -> один самодостаточный html."""
    meta = BOOKS[book]
    html = open(os.path.join(SRC, "template.html"), encoding="utf-8").read()
    lib = lambda n: open(os.path.join(VEND, n), encoding="utf-8").read()
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
    html = html.replace("__PIECES__", json.dumps(pieces))

    V = json.load(open(data_path(book), encoding="utf-8"))
    html = html.replace("__DATA__", json.dumps(V, ensure_ascii=False))

    # подстановка заголовков книги
    d = BOOKS["alekhine"]
    html = (html.replace(f"<title>{d['title']}</title>", f"<title>{meta['title']}</title>")
                .replace(d["eyebrow"], meta["eyebrow"])
                .replace(f"<h1>{d['h1']}</h1>", f"<h1>{meta['h1']}</h1>")
                .replace(d["sub"], meta["sub"])
                .replace(d["credit"], meta["credit"]))

    os.makedirs(DIST, exist_ok=True)
    open(os.path.join(DIST, meta["out"]), "w", encoding="utf-8").write(html)
    print(f"{meta['out']}: {round(len(html)/1024)} KB, вариантов {len(V)}, "
          f"ходов {sum(len(v['moves']) for v in V)}, комментариев {sum(len(v['notes']) for v in V)}")


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
    if cmd == "gen":     [gen(b) for b in targets]
    elif cmd == "eval":  [evaluate(b) for b in targets]
    elif cmd == "build": [build(b) for b in targets]
    elif cmd == "check": check(None if arg == "all" else targets)
    elif cmd == "all":
        for b in targets: gen(b); evaluate(b); gen(b); build(b)
    else: print(__doc__)
