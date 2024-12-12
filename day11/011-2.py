from pathlib import Path

memo = {}


def expands_into(stone, steps):
    if steps == 0:
        return 1
    if (stone, steps) in memo.keys():
        return memo[(stone, steps)]
    if stone == "0":
        out = ["1"]
    elif len(stone) % 2 == 0:
        out = [str(int(stone[: len(stone) // 2])), str(int(stone[len(stone) // 2 :]))]
    else:
        out = [str(int(stone) * 2024)]
    res = sum(expands_into(next_stone, steps - 1) for next_stone in out)
    memo[(stone, steps)] = res
    return res


with open(f"{Path(__file__).parent.resolve()}/011.txt") as file:
    data = file.read().strip()

    tot = 0
    for stone in data.split(" "):
        tot += expands_into(stone, 75)
    print(tot)
