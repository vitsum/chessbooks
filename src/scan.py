import json, re, chess

SAN  = r"(?:O-O-O|O-O|[KQRBN][a-h1-8]?x?[a-h][1-8]|[a-h]x[a-h][1-8](?:=[QRBN])?|[a-h][1-8](?:=[QRBN])?)"
DASH = r"[KQRBN]?[a-h][1-8]-[a-h][1-8]"
NUM  = r"(?:\d+\s*\.(?:\.\.|…)?\s*)?"
TOKR = re.compile(r"(?<![-\w])(" + NUM + r"(?:" + DASH + r"|" + SAN + r")[+#]?[!?]{0,2})(?![-\w])")
SEQ  = re.compile(r"(?:" + TOKR.pattern + r"(?:[\s,]+(?:и\s+)?)?){2,}")

def to_san(tok):
    t = re.sub(r"^\d+\s*\.(?:\.\.|…)?\s*", "", tok)
    t = re.sub(r"[!?]+$", "", t)
    m = re.match(r"^([KQRBN]?)([a-h][1-8])-([a-h][1-8])$", t)
    if m: t = m.group(1) + m.group(3)
    return t

def first_num(tok):
    m = re.match(r"^(\d+)\s*\.(\.\.|…)?", tok)
    if not m: return None
    n = int(m.group(1)); black = bool(m.group(2))
    return (n-1)*2 + (1 if black else 0)      # сколько полуходов уже сделано

def board_at(moves, n):
    b = chess.Board()
    for s in moves[:n]: b.push_san(s)
    return b

def try_line(base, sans):
    b = base.copy(); out=[]
    for s in sans:
        try: m = b.parse_san(s)
        except Exception: return None
        num, w = b.fullmove_number, (b.turn==chess.WHITE)
        san = b.san(m); b.push(m)
        out.append({"san":san,"fen":b.fen(),"from":chess.square_name(m.from_square),
                    "to":chess.square_name(m.to_square),"num":(f"{num}." if w else f"{num}…")})
    return out

def try_plan(base, sans):
    """ходы одной стороны подряд — между ними пропуск хода соперника"""
    b = base.copy(); out=[]
    for i,s in enumerate(sans):
        if i: 
            if b.is_check(): return None
            b.push(chess.Move.null())
        try: m = b.parse_san(s)
        except Exception: return None
        num, w = b.fullmove_number, (b.turn==chess.WHITE)
        san = b.san(m); b.push(m)
        out.append({"san":san,"fen":b.fen(),"from":chess.square_name(m.from_square),
                    "to":chess.square_name(m.to_square),"num":(f"{num}." if w else f"{num}…")})
    return out

def resolve(v, n, sans, tok0):
    cands = []
    fn = first_num(tok0)
    if fn is not None and fn <= len(v["moves"]): cands.append(fn)
    cands += [n, n-1]
    for c in cands:
        if c < 0: continue
        r = try_line(board_at(v["moves"], c), sans)
        if r: return "line", c, r
    for c in [n, n-1, n-2]:
        if c < 0: continue
        base = board_at(v["moves"], c)
        r = try_plan(base, sans)
        if r: return "plan", c, r
        if not base.is_check():                 # план другой стороны: пропускаем ход
            nb = base.copy(); nb.push(chess.Move.null())
            r = try_plan(nb, sans)
            if r: return "plan", c, r
    return None, None, None

BAD_PREFIX = re.compile(r"(на|поля|полях|поле|пункт[ае]?|конями|слонами)\s*$", re.I)

if __name__ == "__main__":
    V = json.load(open("data.json"))
    ok=fail=0
    for v in V:
        for ply, txt in v["notes"].items():
            for m in SEQ.finditer(txt):
                if BAD_PREFIX.search(txt[:m.start()]): continue
                toks = TOKR.findall(m.group(0))
                if len(toks) < 2: continue
                sans = [to_san(t) for t in toks]
                kind, base, pl = resolve(v, int(ply), sans, toks[0])
                mark = {"line":"✔ линия","plan":"✔ план",None:"✘"}[kind]
                print(f"{mark:9} [{v['id']:8} {ply:>3}] {m.group(0).strip()[:56]!r}")
                ok += kind is not None; fail += kind is None
    print("распознано:", ok, "| не вышло:", fail)
