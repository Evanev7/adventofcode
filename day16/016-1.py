from pathlib import Path

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

class LL:
    def __init__(self, score, loc, direction):
        # directions are NESW 0123
        self.score = score
        self.loc = loc
        self.dir = direction
        self.next = None
    def insert(self, score, loc, direction):
        ll = LL(score, loc, direction)
        # Could be recursive, but I think I'm saving the recursion for AOC in Haskell.
        search = self
        while search.next != None and search.score < score:
            search = search.next
        # Insert into LL in sorted position
        ll.next = search.next
        search.next = ll

with open(f"{Path(__file__).parent.resolve()}/016.txt") as file:
    data = file.read().strip()

    spaces = set()
    for y, row in enumerate(data.split("\n")):
        for x, letter in enumerate(row):
            match letter:
                case ".":
                    spaces.add((x,y))
                case "E":
                    goal = (x,y)
                    spaces.add((x,y))
                case "S":
                    start = (x,y)
                    head = LL(0,(x,y),1)
                    spaces.add((x,y))
    
    visited = dict()
    while head.loc != goal:
        for direction in [(head.dir - 1) % 4, head.dir % 4, (head.dir + 1) % 4]:
            neighbour = (head.loc[0] + dirs[direction][0], head.loc[1] + dirs[direction][1])
            score = head.score + (1 if direction == head.dir else 1001)
            if neighbour in spaces and \
                ((neighbour, direction) in visited.keys() and visited[(neighbour, direction)] > score or (neighbour, direction) not in visited.keys()):
                head.insert(score, neighbour, direction)
                visited[(neighbour, direction)] = score

        head = head.next
    
    print("")
    print(head.score)
