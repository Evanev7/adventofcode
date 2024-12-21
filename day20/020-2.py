from pathlib import Path

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

with open(f"{Path(__file__).parent.resolve()}/020.txt") as file:
    data = file.read().strip()

    import time
    now = time.time()

    grid = [list(i) for i in data.split("\n")]
    spaces = set()
    for y, row in enumerate(grid):
        for x, letter in enumerate(row):
            match letter:
                case "S":
                    start = (x,y)
                    spaces.add((x,y))
                case "E":
                    goal = (x,y)
                    spaces.add((x,y))
                case ".":
                    spaces.add((x,y))
    
    path = [start]
    visited = set([start])
    tot = 0
    while path[-1] != goal:
        print(f"\r{len(path)}", end = "")
        for i in range(4):
            neighbour = (path[-1][0] + dirs[i][0], path[-1][1] + dirs[i][1])
            if neighbour in spaces and neighbour not in visited:
                for i, prev in enumerate(path):
                    if abs(prev[0] - neighbour[0]) + abs(prev[1] - neighbour[1]) <= 20 and len(path) - i - (abs(prev[0] - neighbour[0]) + abs(prev[1] - neighbour[1])) >= 100:
                            tot += 1
                
                path.append(neighbour)
                visited.add(neighbour)
    print("")
    print(tot)
    print(time.time() - now)