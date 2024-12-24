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
        curr = int(line)
        w = (0,0,0,0)
        for checked in range(2000):
            nxt = iterate(curr)
            w = (w[1], w[2], w[3], nxt % 10 - curr % 10)
            diff = nxt % 10 - curr % 10
            curr = nxt
            if w not in seq_cache.keys():
                seq_cache[w] = [nxt % 10, set([i])]
            elif i not in seq_cache[w][1]: 
                seq_cache[w][0] += nxt % 10
                seq_cache[w][1].add(i)
    best = (None, [0, set()])
    for key, val in seq_cache.items():
        if val[0] > best[1][0]:
            best = (key, val)
    print(best)