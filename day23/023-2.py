from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/023.txt") as file:
    data = file.read().strip()

    connections = dict()
    for row in data.split("\n"):
        a, b = row.split("-")
        if a not in connections.keys():
            connections[a] = set()
        connections[a].add(b)
        if b not in connections.keys():
            connections[b] = set()
        connections[b].add(a)

    max_coll = set()
    for k in connections.keys():
        kgraphs = set([frozenset([k])])
        while True:
            # Must add an element to progress to next step
            new_kgraphs = set()
            for kgraph in kgraphs:
                all_connections = [connections[i] for i in kgraph]
                for connection in all_connections[0].intersection(*all_connections[1:]):
                    new_kgraphs.add(frozenset([connection, *kgraph]))
            if new_kgraphs == set():
                break
            kgraphs = new_kgraphs
        g = kgraphs.pop()
        if len(g) > len(max_coll):
            max_coll = g
    print(",".join(sorted(list(max_coll))))
