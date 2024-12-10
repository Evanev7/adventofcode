from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/009.txt") as file:
    data = file.read().strip()
    "2333133121414131402"
    import time
    now = time.time()
    # Naive solution baby
    disk = []
    for i, l in enumerate(data):
        match i % 2:
            case 0:
                for _ in range(int(l)):
                    disk.append(i//2)
            case 1:
                for _ in range(int(l)):
                    disk.append(".")
    i=0
    while "." in disk:
        if disk[i] != ".":
            i += 1
            continue
        subj = disk.pop()
        while subj == ".":
            subj = disk.pop()
        if i < len(disk):
            disk[i] = subj
        else:
            disk.append(subj)
        i += 1
        print(f"\rFilled {i}/{len(disk)}      ", end = "")
    print("")
    print(time.time() - now)
    tot = 0
    for i, dat in enumerate(disk):
        tot += i * dat
    print(tot)
    
