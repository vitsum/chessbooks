import chess, json

def build(moves):
    b = chess.Board(); labels=[]; sans=[]
    for san in moves.split():
        n=b.fullmove_number; w=(b.turn==chess.WHITE)
        m=b.parse_san(san); s=b.san(m); b.push(m)
        labels.append(f"{n}.{s}" if w else f"{n}...{s}")
        sans.append(s)
    return sans, labels

V=[]
def add(id, chapter, title, tag, ev, moves, notes, evals=None, subs=None):
    sans, labels = build(moves)
    idx={}
    for k,txt in notes.items():
        if k not in labels: raise SystemExit(f"[{id}] нет хода {k}\n  есть: {labels}")
        idx[str(labels.index(k)+1)] = txt
    V.append({"id":id,"chapter":chapter,"title":title,"tag":tag,"eval":ev,
              "labels":labels,"moves":sans,"notes":idx,
              "evals":{str(len(sans)):tag},"subs":{}})

