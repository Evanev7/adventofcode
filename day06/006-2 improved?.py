class Guard:
    def __init__(self, pos):
        self.pos = pos
        self.dir = 0
        self.visited = {pos: {0}}
    
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
        self.pos = l
        # Check if we've been here before
        if l not in self.visited.keys():
            self.visited[l] = {self.dir}
            return True
        # woah! we've been here before!
        if self.dir not in self.visited[l]:
            self.visited[l].add(self.dir)
            return True
        # in this direction as well!! loop detected!!
        return False
    
    def turn(self):
        self.dir = (self.dir + 1) % 4
    
    def clone(self):
        ng = Guard(self.pos)
        ng.dir = self.dir
        ng.visited = self.visited.copy()
        return ng

def escaped(pos, grid):
    return pos[1] < 0 or pos[1] >= len(grid) or pos[0] < 0 or pos[0] >= len(grid[0])

from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/006.txt") as file:
    data = file.read().strip()
    data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".strip()
    """.#.
...
...
#^.
.#."""
    # Naive solution time
    grid = data.split("\n")
    for i in range(len(grid)):
        # We know the guard starts up
        if "^" in grid[i]:
            start_pos = (grid[i].find("^"),i)
            break
    
    import time
    now = time.time()
    
    guard = Guard(start_pos)
    real_box_pos = set()
    # While still in grid
    while True:
        next_step = guard.next()

        if escaped(next_step, grid):
            break
            
        # fuck exceptions i hate exceptions
        if grid[next_step[1]][next_step[0]] == "#":
            guard.turn()
            continue
        
        # Now we spawn a box in the next_step location, and check that reality.
        ng = guard.clone()
        while True:
            ng_step = ng.next()
            if escaped(ng_step, grid):
                # nothing interesting here
                break
            if grid[ng_step[1]][ng_step[0]] == "#" or ng_step == next_step:
                ng.turn()
            if ng.step() == False:
                # Loop detected!
                real_box_pos.add(next_step)
                break

        guard.step()
        
    print(time.time() - now)
    print(len(guard.visited))
    print(len(real_box_pos))



