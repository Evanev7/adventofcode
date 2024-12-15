from pathlib import Path

def checked_div(a,b):
    if a % b == 0:
        return a//b
    else:
        return None


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
        px, py = 10000000000000+int(px[9:]), 10000000000000+int(py)
        # got our data.
        adotp = ax * px + ay * py
        adotb = ax * bx + ay * by
        bdotp = bx * px + by * py
        asq = ax * ax + ay * ay
        bsq = bx * bx + by * by
        
        n = checked_div((bsq * adotp - adotb * bdotp),(asq * bsq - (adotb * adotb)))
        m = checked_div((- adotb * adotp + asq * bdotp),(asq * bsq - (adotb * adotb)))
        if n != None and m != None:
            tot += (3*n + m)

    print("")
    print(tot)
