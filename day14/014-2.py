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
    
    count = 0
    while True:
        count += 1
        bots = [[(bot[0] + bot[2]) % width, (bot[1] + bot[3]) % height, bot[2], bot[3]] for bot in bots]
        grid = [[0]* width for i in range(height)]
        for bot in bots:
            grid[bot[1]][bot[0]] += 1
        
        for i in range(width-2):
            for j in range(height-2):
                if all([grid[i][j:j+3] == [1,1,1], grid[i+1][j:j+3] == [1,1,1], grid[i+2][j:j+3] == [1,1,1]]):
                    print("\n".join(["".join(map(lambda x: " " if x == 0 else "1", i)) for i in grid]))
                    print(count, i, j)
                    input()


    