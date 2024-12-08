from pathlib import Path

# condensed version of
# M S
#  A
# M S
search = ["MSAMS","SSAMM", "MMASS", "SMASM"]

with open(f"{Path(__file__).parent.resolve()}/004.txt") as file:
    data = file.read().strip()
    grid = data.split("\n")
    tot = 0

    for i in range(len(grid)-2):
        for j in range(len(grid[0])-2):
            chunk = "".join([grid[i][j], grid[i][j+2], grid[i+1][j+1], grid[i+2][j], grid[i+2][j+2]])
            if chunk in search:
                tot += 1


    print(tot)
