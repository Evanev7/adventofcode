from pathlib import Path

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

with open(f"{Path(__file__).parent.resolve()}/020.txt") as file:
    data = file.read().strip()
    #data = \
    """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""
    #data = \
    """S..
##.
E.."""


    grid = [list(i) for i in data.split("\n")]
    spaces = dict()
    for y, row in enumerate(grid):
        print(row)
        for x, letter in enumerate(row):
            match letter:
                case "S":
                    start = (x,y)
                    spaces[(x,y)] = 0
                case "E":
                    goal = (x,y)
                    spaces[(x,y)] = 0
                case ".":
                    spaces[(x,y)] = 0
    
    
    curr = start
    curr_dir = 0
    curr_score = 0
    to_visit = set()
    while curr != goal:
        for i in range(curr_dir-1,curr_dir+2):
            neighbour = (curr[0] + dirs[i%4][0], curr[1] + dirs[i%4][1])
            if neighbour in spaces.keys():
                to_visit.add((neighbour, i%4))
        curr, curr_dir = to_visit.pop()
        curr_score += 1
        spaces[curr] = curr_score
    
    adjacencies = set()
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            for i in range(4):
                mid = (x + dirs[i][0], y + dirs[i][1])
                jumpto = (x+2*dirs[i][0], y+2*dirs[i][1])
                if jumpto in spaces.keys() and (x,y) in spaces.keys() and spaces[jumpto] > spaces[(x,y)] and mid not in spaces.keys():
                    adjacencies.add((spaces[(x,y)], spaces[jumpto]))

    ordered = dict()
    for adj in adjacencies:
        if adj[1] - adj[0] - 2 in ordered.keys():
            ordered[adj[1] - adj[0] - 2].add(adj)
        else:
            ordered[adj[1] - adj[0] - 2] = set([adj])
    tot = 0
    for key in ordered.keys():
        if key >= 100:
            tot += len(ordered[key])
    print(tot)

    print(all(i in spaces.values() for i in range(0,len(spaces.values()))))
    print(len(spaces.values()))