from pathlib import Path

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

def heur(pos, goal):
    return abs(pos[0]-goal[0]) + abs(pos[1]-goal[1])

# Copied from day 16
class LL:
    def __init__(self, score, loc, rs):
        # directions are NESW 0123
        self.real_score = rs
        self.score = score
        self.loc = loc
        self.next = None
    def insert(self, score, loc, rs):
        ll = LL(score, loc, rs)
        # Could be recursive, but I think I'm saving the recursion for AOC in Haskell.
        search = self
        while search.next != None and search.score < score:
            search = search.next
        # Insert into LL in sorted position
        ll.next = search.next
        search.next = ll

with open(f"{Path(__file__).parent.resolve()}/018.txt") as file:
    data = file.read().strip()

    fallen = set()
    for row in data.split("\n")[:1024]:
        fallen.add(tuple(map(int, row.split(","))))

    spaces = set([(i,j) for i in range(71) for j in range(71)]) - fallen
    
    goal = (70,70)
    for (i, row) in enumerate(data.split("\n")[1024:]):
        just_fallen = tuple(map(int, row.split(",")))
        print(i, just_fallen)
        spaces.remove(just_fallen)
        head = LL(0, (0,0), 0)
        visited = dict()
        while head.loc != goal:
            for direction in range(4):
                neighbour = (head.loc[0] + dirs[direction][0], head.loc[1] + dirs[direction][1])
                rs = head.real_score + 1
                # A* modification!
                score = rs + heur(neighbour, goal)
                if neighbour in spaces and neighbour not in visited.keys():
                    head.insert(score, neighbour, rs)
                    visited[neighbour] = score
            head = head.next
    
    print("")
    print(head.score)
