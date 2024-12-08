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
                forward = (2 * pairlist[i][0] - pairlist[j][0], 2 * pairlist[i][1] - pairlist[j][1])
                backward = (2 * pairlist[j][0] - pairlist[i][0], 2 * pairlist[j][1] - pairlist[i][1])
                if 0 <= forward[0] and forward[0] < bounds[0] and 0 <= forward[1] and forward[1] < bounds[1]:
                    antinodes.add(forward)
                if 0 <= backward[0] and backward[0] < bounds[0] and 0 <= backward[1] and backward[1] < bounds[1]:
                    antinodes.add(backward)
    print(len(antinodes))


