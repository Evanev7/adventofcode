from pathlib import Path
def find_item(disk, ind):
    for i,file in enumerate(disk):
        if file[0] == ind:
            return i

with open(f"{Path(__file__).parent.resolve()}/009.txt") as file:
    data = file.read().strip()
    "2333133121414131402"
    import time
    now = time.time()
    # Different solution baby
    # We need to transform 131...512 into 10211...5
    # Gonna try and move every file once.
    # Our model of a disk is a file index then it's length, and the gap that follows it.
    disk = [[i,int(data[2*i]), int(data[2*i+1])] for i in range(len(data)//2)]
    disk.append([disk[-1][0]+1, int(data[-1]), 0])
    i = disk[-1][0]
    while i > 0:
        print(f"\rProcessing {len(disk)-i}/{len(disk)}     ", end="")

        ind = find_item(disk, i)
        pred = disk[ind-1]
        item = disk[ind]
        for j in range(ind):
            # If we find enough space for our item
            if disk[j][2] >= item[1]:
                disk[ind-1][2] += item[1] + item[2]
                item[2] = disk[j][2] - item[1]
                disk[j][2] = 0
                disk.pop(ind)
                disk.insert(j+1, item)
                break
        i -= 1


    print("")
    print(time.time() - now)
    tot = 0
    # could do some fancy stuff but im just gonna expand the disk
    full_disk = []
    for file in disk:
        for _ in range(file[1]):
            full_disk.append(file[0])
        for _ in range(file[2]):
            full_disk.append(0)
    for i, dat in enumerate(full_disk):
        tot += i * dat
    print(tot)
    
