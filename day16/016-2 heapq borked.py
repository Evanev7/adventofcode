from pathlib import Path
import heapq

dirs = [(0,-1), (1,0), (0,1), (-1,0)]

with open(f"{Path(__file__).parent.resolve()}/016.txt") as file:
    data = file.read().strip()

    import time
    now = time.time()

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
                    queue = [(0,[(x,y)],1)]
                    spaces.add((x,y))
    
    visited = dict()
    spots = set()
    max_score = 99999999999
    finishers = []
    while queue[0][0] <= max_score:
        head = queue[0]
        if head[1][0] == goal:
            max_score = head[0]
            spots |= set(head[1])
            finishers.append(head)

        flag = False

        for direction in [(head[2] - 1) % 4, head[2] % 4, (head[2] + 1) % 4]:
            neighbour = (head[1][0][0] + dirs[direction][0], head[1][0][1] + dirs[direction][1])
            score = head[0] + (1 if direction == head[2] else 1001)
            if neighbour in spaces and \
                ((neighbour, direction) in visited.keys() and visited[(neighbour, direction)] >= score or (neighbour, direction) not in visited.keys()):
                if not flag:
                    heapq.heappushpop(queue, (score, [neighbour, *head[1]], direction))
                    flag = True
                else:
                    heapq.heappush(queue, (score, [neighbour, *head[1]], direction))
                visited[(neighbour, direction)] = score
    
    print("")
    print(max_score)
    print(len(spots))
    print(len(finishers))
    print(time.time() - now)
