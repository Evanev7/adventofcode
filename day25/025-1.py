from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/025.txt") as file:
    data = file.read().strip()
    #data = \
    """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

    keys = []
    locks = []
    for klock in data.split("\n\n"):
        if klock[0] == ".":
            keys.append(tuple(6 - "".join(i).find("#" ) for i in zip(*klock.split("\n"))))
        else:
            locks.append(tuple("".join(i).find(".") - 1 for i in zip(*klock.split("\n"))))
    print(keys, locks)
    matching = set()
    for key in keys:
        for lock in locks:
            for i in range(5):
                if key[i] + lock[i] > 5:
                    break
            else:
                matching.add((key, lock))
    print(len(matching))
    