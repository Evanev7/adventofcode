from pathlib import Path

class Plot:
    def __init__(self, coord):
        self.plots = set([coord])
    def maybe_add_plot(self, coord):
        if (coord[0] + 1, coord[1]) in self.plots \
            or (coord[0] - 1, coord[1]) in self.plots \
            or (coord[0], coord[1] + 1) in self.plots \
            or (coord[0], coord[1] - 1) in self.plots:
            self.plots.add(coord)
            return True
        return False
    def area(self):
        return len(self.plots)
    def perimeter(self):
        tot = 0
        for plot in self.plots:
            if (plot[0] + 1, plot[1]) not in self.plots:
                tot += 1
            if (plot[0] - 1, plot[1]) not in self.plots:
                tot += 1
            if (plot[0], plot[1] + 1) not in self.plots:
                tot += 1
            if (plot[0], plot[1] - 1) not in self.plots:
                tot += 1
        return tot

with open(f"{Path(__file__).parent.resolve()}/012.txt") as file:
    data = file.read().strip()
    """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
    grid = data.split("\n")

    # Dict[Str, List[Plot]]
    regions = {}

    for j, row in enumerate(grid):
        for i, letter in enumerate(row):
            print(f"\r Progress {i + j * len(row)}/{len(grid) * len(row)} on coord ({i},{j}):'{letter}'.", end="")
            if letter not in regions.keys():
                regions[letter] = [Plot((i,j))]
                continue
            merge = []
            for index, plot in enumerate(regions[letter]):
                success = plot.maybe_add_plot((i,j))
                if success:
                    merge.append(index) 
            if merge == []:
                regions[letter].append(Plot((i,j)))
                continue
            # The rest of this is merging plot cleanup.
            ns = set()
            for index in merge:
                ns |= regions[letter][index].plots
            merged = Plot((0,0))
            merged.plots = ns
            # Reverse so we can remove from list safely.
            for index in merge[::-1]:
                regions[letter].pop(index)
            regions[letter].append(merged)
                

    print("")
    tot = 0
    for letter, plots in regions.items():
        for plot in plots:
            print(f"{letter} plot contributing {plot.area() * plot.perimeter()}")
            tot += plot.area() * plot.perimeter()
    print("")
    print(tot)
