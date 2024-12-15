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

    grid, moves = data.split("\n\n")
    moves = "".join(moves.split("\n"))

    grid = [list(i) for i in grid.split("\n")]
    walls = set()
    boxes = set()
    bot = (0,0)
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            match grid[j][i]:
                case "#":
                    walls.add((i,j))
                case "O":
                    boxes.add((i,j))
                    grid[j][i] = "."
                case "@":
                    bot = (i,j)
                    grid[j][i] = "."
    for move in moves:
        match move:
            case "^":
                direction = (0,-1)
            case ">":
                direction = (1,0)
            case "v":
                direction = (0,1)
            case "<":
                direction = (-1,0)
        step = (bot[0] + direction[0], bot[1] + direction[1])
        search = step + tuple()
        while search in boxes:
            search = (search[0] + direction[0], search[1] + direction[1])
        if search in walls:
            continue
        bot = step
        if step in boxes:
            boxes.remove(step)
            boxes.add(search)
    
    tot = 0
    for box in boxes:
        tot += 100 * box[1] + box[0]
        grid[box[1]][box[0]] = "O"
    grid[bot[1]][bot[0]] = "@"
    print("\n".join(["".join(i) for i in grid]))
    print(tot)



        

