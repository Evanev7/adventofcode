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
    def sides(self):
        # We can probably be pretty inefficient with this. I think, just check if you are a top/left-most segment of a perimeter.
        # We are in a
        #  -y->
        # |
        # x
        # |
        # v
        # coordinate system
        tot = 0
        for plot in self.plots:
            # If we are a right-facing perimeter and our above is empty or both above and above-right are filled.
            if (plot[0] + 1, plot[1]) not in self.plots \
                and ((plot[0], plot[1] + 1) not in self.plots \
                or ((plot[0], plot[1] + 1) in self.plots and (plot[0] + 1, plot[1] + 1) in self.plots)):
                tot += 1
            # If we are a left-facing perimeter and our above is empty or both above and above-left are filled.
            if (plot[0] - 1, plot[1]) not in self.plots \
                and ((plot[0], plot[1] + 1) not in self.plots \
                or ((plot[0], plot[1] + 1) in self.plots and (plot[0] - 1, plot[1] + 1) in self.plots)):
                tot += 1
            # If we are a down-facing perimeter and our left is empty or both left and down-left are filled.
            if (plot[0], plot[1] + 1) not in self.plots \
                and ((plot[0] - 1, plot[1]) not in self.plots \
                or ((plot[0] - 1, plot[1]) in self.plots and (plot[0] - 1, plot[1] + 1) in self.plots)):
                tot += 1
            # If we are an up-facing perimeter and our left is empty or both left and up-left are filled.
            if (plot[0], plot[1] - 1) not in self.plots \
                and ((plot[0] - 1, plot[1]) not in self.plots \
                or ((plot[0] - 1, plot[1]) in self.plots and (plot[0] - 1, plot[1] - 1) in self.plots)):
                tot += 1
        return tot

with open(f"{Path(__file__).parent.resolve()}/012.txt") as file:
    data = file.read().strip()
    """EEEEE
EXXXX
EEEEE
EXXXX
EEEEE"""
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
            a = plot.area()
            s = plot.sides()
            print(f"{letter} plot contributing {a:<4}*{s:<4}={a*s:<4}")
            tot += a*s
    print("")
    print(tot)
