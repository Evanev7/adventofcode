from pathlib import Path


class Walker:
    def __init__(self, pos, grid):
        self.pos = [pos]
        self.grid = grid
        self.bounds = (len(grid[0]), len(grid))
        self.paths = 1
    def walk(self):
        for i in range(1,10):
            self.step(i)
        return len(self.pos)
    def step(self, i):
        out = []
        # Inefficient but should do it
        for pos in self.pos:
            for ofs in [(-1,0), (1,0), (0,1), (0,-1)]:
                next_pos = (pos[0]+ofs[0], pos[1]+ofs[1])
                if 0 <= next_pos[0] and next_pos[0] < self.bounds[0] and 0 <= next_pos[1] and next_pos[1] < self.bounds[1] and self.grid[next_pos[1]][next_pos[0]] == str(i):
                    out.append(next_pos)
        self.pos = out

    

with open(f"{Path(__file__).parent.resolve()}/010.txt") as file:
    data = file.read().strip()
    data = """.....0.
..4321.
..5..2.
..6543.
..7..4.
..8765.
..9...."""

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
