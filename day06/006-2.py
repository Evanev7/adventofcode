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

from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/006.txt") as file:
    data = file.read().strip()
    # Naive solution time
    grid = data.split("\n")
    for i in range(len(grid)):
        # We know the guard starts up
        if "^" in grid[i]:
            start_pos = (grid[i].find("^"),i)
            break
    
    guard = Guard(start_pos)
    # While still in grid
    while True:
        next_step = guard.next()
        # fuck exceptions i hate exceptions
        if next_step[1] < 0 or next_step[1] >= len(grid) or next_step[0] < 0 or next_step[0] >= len(grid[0]):
            break
        if grid[next_step[1]][next_step[0]] == "#":
            guard.turn()
        guard.step()
    print(len(guard.visited))

    # Now we know all the places we could put a box, let's try stupidly checking all of them.
    # We need to also record all our previous states and see if we are repeating a state.
    import time
    now = time.time()
    real_box_pos = set()
    for potential_box_pos in guard.visited:
        guard = Guard(start_pos)
        while True:
            next_step = guard.next()
            # fuck exceptions i hate exceptions
            if next_step[1] < 0 or next_step[1] >= len(grid) or next_step[0] < 0 or next_step[0] >= len(grid[0]):
                break
            if grid[next_step[1]][next_step[0]] == "#" or next_step == potential_box_pos:
                guard.turn()
            # If we've found a loop
            if guard.step() == False:
                real_box_pos.add(potential_box_pos)
                break
    print(len(real_box_pos))
    print(time.time() - now)



