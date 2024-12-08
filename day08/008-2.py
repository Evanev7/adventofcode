from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/008.txt") as file:
    data = file.read().strip()
    """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    grid = data.split("\n")
    bounds = (len(grid[0]), len(grid))
    # Sketch:
    # Construct
    # tower -> coords
    # Use pairs of coords to get set(antinodes)
    towers = {}
    for y,row in enumerate(grid):
        for x,char in enumerate(row):
            if char == "." or char == "\n":
                continue
            if char in towers.keys():
                towers[char].append((x,y))
            else:
                towers[char] = [(x,y)]
    
    antinodes = set()
    for pairlist in towers.values():
        # List of unique pairs of towers.
        for i in range(len(pairlist)):
            for j in range(i+1, len(pairlist)):
                # Bounds check
                forward = (pairlist[i][0] - pairlist[j][0], pairlist[i][1] - pairlist[j][1])
                backward = (pairlist[j][0] - pairlist[i][0], pairlist[j][1] - pairlist[i][1])
                fstart = (pairlist[i][0], pairlist[i][1])
                bstart = (pairlist[j][0], pairlist[j][1])
                while 0 <= fstart[0] and fstart[0] < bounds[0] and 0 <= fstart[1] and fstart[1] < bounds[1]:
                    antinodes.add(fstart)
                    fstart = (fstart[0] + forward[0], fstart[1] + forward[1])
                while 0 <= bstart[0] and bstart[0] < bounds[0] and 0 <= bstart[1] and bstart[1] < bounds[1]:
                    antinodes.add(bstart)
                    bstart = (bstart[0] + backward[0], bstart[1] + backward[1])
    print(len(antinodes))


