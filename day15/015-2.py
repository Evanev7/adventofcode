from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/015.txt") as file:
    data = file.read().strip()
    """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""
    """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^"""

    grid, moves = data.split("\n\n")
    moves = "".join(moves.split("\n"))

    grid = [list(i) for i in grid.split("\n")]
    walls = set()
    left_boxes = set()
    right_boxes = set()
    bot = (0,0)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            match grid[j][i]:
                case "#":
                    walls.add((2*i,j))
                    walls.add((2*i+1,j))
                    grid[j][i] = "##"
                case "O":
                    left_boxes.add((2*i,j))
                    right_boxes.add((2*i+1,j))
                    grid[j][i] = ".."
                case "@":
                    bot = (2*i,j)
                    grid[j][i] = ".."
                case ".":
                    grid[j][i] = ".."
    for move in moves:
        ng = []
        for i,row in enumerate(grid):
            ng.append([])
            for j in row:
                ng[i].append(j[0])
                ng[i].append(j[0])
        for box in left_boxes:
            ng[box[1]][box[0]] = "["
            ng[box[1]][box[0]+1] = "]"
        ng[bot[1]][bot[0]] = "@"
        match move:
            case "<":
                direction = (-1,0)
            case ">":
                direction = (1,0)
            case "^":
                direction = (0,-1)
            case "v":
                direction = (0,1)
        moved_boxes = set()
        step = (bot[0]+direction[0], bot[1]+direction[1])
        if step in left_boxes:
            moved_boxes.add(step)
        elif step in right_boxes:
            moved_boxes.add((step[0]-1, step[1]))
        else:
            # Nothing to move case: handled
            if step in walls:
                continue
            bot = step
            continue
        active = moved_boxes.copy()
        flag = False
        while len(active) > 0:
            cur = active.pop()
            # not very DRY of you there bozo
            # does this run into order problems???? it shouldnt because it just scans through
            # maybe should be recursive thinking about it
            # oh well
            # Left of the box moved
            nex1 = (cur[0] + direction[0], cur[1] + direction[1])
            if nex1 in left_boxes and nex1 not in moved_boxes:
                active.add(nex1)
                moved_boxes.add(nex1)
            if nex1 in right_boxes and (nex1[0]-1, nex1[1]) not in moved_boxes:
                active.add((nex1[0]-1, nex1[1]))
                moved_boxes.add((nex1[0]-1, nex1[1]))
            # Right of the box moved
            nex2 = (cur[0] + direction[0]+1, cur[1] + direction[1])
            if nex2 in left_boxes and nex2 not in moved_boxes:
                active.add(nex2)
                moved_boxes.add(nex2)
            if nex2 in right_boxes and (nex2[0]-1, nex2[1]) not in moved_boxes:
                active.add((nex2[0]-1, nex2[1]))
                moved_boxes.add((nex2[0]-1, nex2[1]))
            if nex1 in walls or nex2 in walls:
                flag = True
        # everything is stuck case: handled
        if flag: continue
        # just gotta move all the boxes now
        for box in moved_boxes:
            left_boxes.remove(box)
            right_boxes.remove((box[0]+1,box[1]))
        for box in moved_boxes:
            left_boxes.add((box[0]+direction[0], box[1]+direction[1]))
            right_boxes.add((box[0]+direction[0]+1, box[1]+direction[1]))
        bot = step



    tot = 0
    ng = []
    for i,row in enumerate(grid):
        ng.append([])
        for j in row:
            ng[i].append(j[0])
            ng[i].append(j[0])
    for box in left_boxes:
        tot += 100 * box[1] + box[0]
        ng[box[1]][box[0]] = "["
        ng[box[1]][box[0]+1] = "]"
    ng[bot[1]][bot[0]] = "@"
    print("\n".join(["".join(i) for i in ng]))
    print(tot)



        

