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

# ================= оценки Stockfish =================
import os
if os.path.exists(CP_IN):
    CP = json.load(open(CP_IN))
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

json.dump(V, open(DATA_OUT,"w"), ensure_ascii=False)
print("вариантов:", len(V), "| ходов всего:", sum(len(v["moves"]) for v in V),
      "| комментариев:", sum(len(v["notes"]) for v in V))
