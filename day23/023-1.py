from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/023.txt") as file:
    data = file.read().strip()
    #data = \
    """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""
    connections = dict()
    for row in data.split("\n"):
        a, b = row.split("-")
        if a not in connections.keys():
            connections[a] = set()
        connections[a].add(b)
        if b not in connections.keys():
            connections[b] = set()
        connections[b].add(a)
    
    collected = set()
    for k, v in connections.items():
        if k[0] != "t":
            continue
        # Find all triads containing tx
        for d1 in v:
            if d1 == k:
                continue
            for d2 in connections[d1]:
                if d2 == k:
                    continue
                if k in connections[d2]:
                    collected.add(tuple(sorted([k, d1, d2])))
    print(len(collected))