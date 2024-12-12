from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/011.txt") as file:
    data = file.read().strip()

    import time

    now = time.time()
    steps = 25
    stones = list(map(lambda x: (int(x), steps, set()), data.split(" ")))
    tot = 0
    memo_buffer = [0]*75
    memo = {}
    prev_rem = 9999
    while len(stones) > 0:
        stone, rem = stones.pop()
        active -= resolves
        active.add((stone, rem))
        if rem == 0:
            tot += 1
            for item in active:
                if item in memo.keys():
                    memo[item] += 1
                else:
                    memo[item] = 1
            continue
        if (stone, rem) in memo.keys():
            tot += memo[(stone, rem)]
            continue
        if len(stones) > 0:
            stones[-1][2].add((stone, rem))
        if stone == 0:
            stones.append((1, rem - 1, set()))
        elif len(str(stone)) % 2 == 0:
            stones.append((int(str(stone)[: len(str(stone)) // 2]), rem - 1, set()))
            stones.append((int(str(stone)[len(str(stone)) // 2 :]), rem - 1, set()))
        else:
            stones.append((stone * 2024, rem - 1, set()))
        prev_rem = rem
    print("")
    print(tot)
    print(time.time() - now)
