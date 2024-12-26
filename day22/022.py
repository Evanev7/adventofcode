from pathlib import Path

MOD = 16777216
def iterate(num):
    a = ((num * 64) ^ num) % MOD
    b = ((a // 32) ^ a) % MOD
    c = ((b * 2048) ^ b) % MOD
    return c

with open(f"{Path(__file__).parent.resolve()}/022.txt") as file:
    data = file.read().strip()

    seq_cache = dict()

    for i,line in enumerate(data.split("\n")):
        checked = set()
        curr = int(line)
        w = (None,None,None,None)
        for _ in range(2000):
            nxt = iterate(curr)
            w = (w[1], w[2], w[3], nxt % 10 - curr % 10)
            diff = nxt % 10 - curr % 10
            curr = nxt
            if None in w:
                continue
            if w not in seq_cache.keys():
                seq_cache[w] = 0
            if w not in checked: 
                seq_cache[w] += nxt % 10
                checked.add(w)
    print(max(seq_cache.values()))