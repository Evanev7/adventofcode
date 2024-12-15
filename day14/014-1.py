from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/014.txt") as file:
    data = file.read().strip()
    """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""

    # Formatted as [[px, py, vx, vy], ..]
    bots = []
    for i in data.split("\n"):
        ps, vs = [j.split(",") for j in i.split(" ")]
        bots.append([int(ps[0][2:]), int(ps[1]), int(vs[0][2:]), int(vs[1])])
    
    # Game dev coordinates
    # +-x->
    # |
    # y
    # |
    # V

    steps = 100
    width = 101
    height = 103
    quadrs = [0,0,0,0]
    for bot in bots:
        finalpos = (bot[0] + steps * bot[2]) % width, (bot[1] + steps * bot[3]) % height
        if finalpos[0] == width//2 or finalpos[1] == height//2:
            print("skipping!")
            continue
        quadr = 2 * (finalpos[0] < width//2) + int(finalpos[1] < height//2)
        quadrs[quadr] += 1
        print(finalpos)
    tot = 1
    for quad in quadrs:
        tot *= quad
    print(tot)
    