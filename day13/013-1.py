from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/013.txt") as file:
    data = file.read().strip()

    chunks = data.split("\n\n")
    tot = 0
    for chunk in chunks:
        a,b,p = chunk.split("\n")
        ax, ay = a.split(", Y+")
        ax, ay = int(ax[12:]), int(ay)
        bx, by = b.split(", Y+")
        bx, by = int(bx[12:]), int(by)
        px, py = p.split(", Y=")
        px, py = int(px[9:]), int(py)
        # got our data.

        # soln = (int,int)
        soln = None
        # at max 100 a presses
        for i in range(101):
            # Skip once we've overshot
            if i * ax > px or i * ay > py:
                break 
            for j in range(100):
                # Skip once we've overshot
                if (i * ax + j * bx) > px or (i * ay + j * by) > py:
                    break
                # Solution found
                if (i * ax + j * bx) == px and (i * ay + j * by) == py:
                    # If prev solution was more expensive, update
                    if soln == None or soln[0] * 3 + soln[1] > (i * 3 + j * 1):
                        soln = (i,j)
        if soln != None:
            tot += 3 * soln[0] + soln[1]
    print(tot)
