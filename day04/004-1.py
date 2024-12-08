from pathlib import Path

dirs = [(i,j) for i in range(-1,2) for j in range(-1,2) if not (i == 0 and j == 0)]
search = "XMAS"

with open(f"{Path(__file__).parent.resolve()}/004.txt") as file:
    data = file.read().strip()
    grid = data.split("\n")
    tot = 0
    for direction in dirs:
        # Assume a rectangle
        # Should be 0 unless direction[0] == -1, then it should be 3.
        xstart = 0 if direction[0] >= 0 else 3
        ystart = 0 if direction[1] >= 0 else 3
        # Should be len(row) unless direction[0] == 1 then it should be len(row) - 3?? -4??
        xend = len(grid) if direction[0] <= 0 else len(grid) - 3
        yend = len(grid[0]) if direction[1] <= 0 else len(grid[0]) - 3
        for x in range(xstart, xend):
            for y in range(ystart, yend):
                substr = "".join([grid[x + k * direction[0]][y+k*direction[1]] for k in range(len(search))])
                if substr == search:
                    tot +=1
    print(tot)
