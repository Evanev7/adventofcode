from pathlib import Path


class Walker:
    def __init__(self, pos, grid):
        self.pos = set([pos])
        self.grid = grid
        self.bounds = (len(grid[0]), len(grid))
    def walk(self):
        for i in range(1,10):
            self.step(i)
        return len(self.pos)
    def step(self, i):
        out = set()
        for pos in self.pos:
            for ofs in [(-1,0), (1,0), (0,1), (0,-1)]:
                next_pos = (pos[0]+ofs[0], pos[1]+ofs[1])
                # print(next_pos)
                # print(f"checking for {i} at {next_pos}: {0 <= next_pos[0]} and {next_pos[0] < self.bounds[0]} and {0 <= next_pos[1]} and {next_pos[1] < self.bounds[1]} and {self.grid[next_pos[1]][next_pos[0]]}")
                
                if 0 <= next_pos[0] and next_pos[0] < self.bounds[0] and 0 <= next_pos[1] and next_pos[1] < self.bounds[1] and self.grid[next_pos[1]][next_pos[0]] == str(i):
                    out.add(next_pos)
        self.pos = out

    

with open(f"{Path(__file__).parent.resolve()}/010.txt") as file:
    data = file.read().strip()
    """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""

    grid = data.split("\n")

    zeroes = []
    for x in range(len(grid[0])): 
        for y in range(len(grid)):
            if grid[y][x] == "0":
                zeroes.append((x,y)) 
    tot = 0
    for startpos in zeroes:
        tot += Walker(startpos, grid).walk()
    print(tot)
