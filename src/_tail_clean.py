# ================= вехи оценки и подварианты =================
EVALS = {}
SUBS = {}

for v in V:
    labels = v["labels"]
    def ply_of(k, vid=v["id"], labels=labels):
        if k not in labels: raise SystemExit(f"[{vid}] нет хода {k}\n  есть: {labels}")
        return labels.index(k)+1
    for k, sym in EVALS.get(v["id"], {}).items():
        v["evals"][str(ply_of(k))] = sym
    for k, items in SUBS.get(v["id"], {}).items():
        n = ply_of(k)
        for cap, mv, when in items:
            bb = chess.Board()
            for san in v["moves"][:(n-1 if when=="before" else n)]: bb.push_san(san)
            plies=[]
            for san in mv.split():
                num, w = bb.fullmove_number, (bb.turn==chess.WHITE)
                m = bb.parse_san(san); s2 = bb.san(m); bb.push(m)
                plies.append({"san":s2,"fen":bb.fen(),
                              "from":chess.square_name(m.from_square),
                              "to":chess.square_name(m.to_square),
                              "num":(f"{num}." if w else f"{num}…")})
            v["subs"].setdefault(str(n),[]).append({"cap":cap,"plies":plies})

# ================= кликабельные ходы прямо в тексте комментариев =================
import scan as _sc
for v in V:
    v["isubs"] = {}
    for ply, txt in list(v["notes"].items()):
        parts, last, hit = [], 0, False
        for m in _sc.SEQ.finditer(txt):
            if _sc.BAD_PREFIX.search(txt[:m.start()]): continue
            toks = _sc.TOKR.findall(m.group(0))
            if len(toks) < 2: continue
            sans = [_sc.to_san(t) for t in toks]
            kind, base, pl = _sc.resolve(v, int(ply), sans, toks[0])
            if not kind: continue
            sid = str(len(v["isubs"]))
            v["isubs"][sid] = {"kind":kind, "startFen":_sc.board_at(v["moves"], base).fen(), "plies":pl}
            frag, trail = m.group(0), ""
            while frag and frag[-1] in " ,.;": trail = frag[-1] + trail; frag = frag[:-1]
            parts += [txt[last:m.start()], f'<a class="inl" data-s="{sid}">{frag}</a>', trail]
            last = m.start() + len(m.group(0)); hit = True
        if hit:
            parts.append(txt[last:]); v["notes"][ply] = "".join(parts)

# ================= что по умолчанию вне тренировки =================
# Тренажёр просит повторить ходы чёрных, поэтому две группы вариантов он
# по умолчанию не берёт (в приложении их можно включить руками):
#   * партии целиком — их не учат наизусть;
#   * линии, где показан плохой ход ЗА ТУ СТОРОНУ, ЗА КОТОРУЮ ИДЁТ РЕПЕРТУАР
#     («Ловушка: 4…Kf6?») — просить повторить такой ход нельзя. Плохие ходы
#     соперника наоборот полезны: их учатся наказывать, такие варианты остаются.
import re as _re
_NUMMOVE = _re.compile(r"^(\d+)(\.\.\.|…|\.)(.*)$")
_SAN     = _re.compile(r"^(?:O-O(?:-O)?|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](?:=[QRBN])?)"
                       r"[+#]?([?!]*)$")

def _own_blunder(title, own=None):
    """В заголовке варианта плохим помечен ход своей стороны?"""
    own = own or globals().get("SIDE", "b")
    side = None
    for w in title.replace("(", " ").replace(")", " ").split():
        m = _NUMMOVE.match(w)
        if m:
            side, body = ("b" if m.group(2) in ("…", "...") else "w"), m.group(3)
        else:
            body = w
            side = "b" if side == "w" else None      # ход без номера идёт за белым
        sm = _SAN.match(body)
        if not sm:
            side = side if m else None
            continue
        if side == own and "?" in sm.group(1).replace("!?", ""):
            return True
    return False

_off = []
for v in V:
    why = ("партия целиком" if "Партии целиком" in v["chapter"]
           else "ошибка за свою сторону" if _own_blunder(v["title"]) else None)
    v["off"] = bool(why)
    if why: _off.append((v["id"], why, v["title"]))
if _off:
    print("вне тренировки по умолчанию:", len(_off))
    for i, why, t in _off:
        print(f"    {i:16} {why:18} {t}")

# ================= оценки Stockfish =================
import os
if os.path.exists(CP_IN):
    CP = json.load(open(CP_IN, encoding="utf-8"))
    for v in V:
        if v["id"] in CP: v["cp"] = CP[v["id"]]

# варианты одной главы должны идти подряд, в каком бы порядке их ни добавили
_order = {}
for v in V:
    _order.setdefault(v["chapter"], len(_order))
V.sort(key=lambda v: _order[v["chapter"]])

# в превью варианта убираем общее начало главы, чтобы строки различались
from itertools import groupby
for _, grp in groupby(V, key=lambda x: x["chapter"]):
    grp = list(grp)
    k = 0
    while all(len(v["labels"]) > k for v in grp) and len({v["labels"][k] for v in grp}) == 1:
        k += 1
    for v in grp:
        tail = v["labels"][k:k+8]
        v["line"] = ("… " if k else "") + " ".join(tail) + (" …" if len(v["labels"]) > k+8 else "")
        del v["labels"]

# encoding указываем явно: без него на Windows файл пишется в cp1251 и сборка падает
json.dump(V, open(DATA_OUT, "w", encoding="utf-8"), ensure_ascii=False)
print("вариантов:", len(V), "| ходов всего:", sum(len(v["moves"]) for v in V),
      "| комментариев:", sum(len(v["notes"]) for v in V))
