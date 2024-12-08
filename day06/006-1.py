class Guard:
    def __init__(self, x: int, y: int):
        self.pos = [x,y]
        self.dir = 0
        self.visited = set()
        self.visited.add((x,y))
    
    def next(self):
        match self.dir:
            case 0:
                return (self.pos[0], self.pos[1]-1)
            case 1:
                return (self.pos[0]+1, self.pos[1])
            case 2:
                return (self.pos[0], self.pos[1]+1)
            case 3:
                return (self.pos[0]-1, self.pos[1])
    
    def step(self):
        l = self.next()
        self.visited.add(l)
        self.pos = l
    
    def turn(self):
        self.dir = (self.dir + 1) % 4

from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/006.txt") as file:
    data = file.read()
    # Naive solution time
    grid = data.split("\n")
    for i in range(len(grid)):
        # We know the guard starts up
        if "^" in grid[i]:
            guard = Guard(grid[i].find("^"),i)
            break
    
    # While still in grid
    while True:
        next_step = guard.next()
        try: 
            if grid[next_step[1]][next_step[0]] == "#":
                guard.turn()
        except IndexError:
            break
        guard.step()
    print(len(guard.visited))