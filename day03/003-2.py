digits = ["0","1","2","3","4","5","6","7","8","9"]

def check_slice(slice):
    if slice[0:4] == "do()":
        return True
    if slice[0:7] == "don't()":
        return False
    if slice[0:4] != "mul(":
        return
    int1 = 0
    int2 = 0
    index = 4
    while slice[index] in digits:
        int1 *= 10
        int1 += int(slice[index])
        index += 1
    if slice[index] != ",":
        return
    index += 1
    while slice[index] in digits:
        int2 *= 10
        int2 += int(slice[index])
        index += 1
    if slice[index] == ")":
        return int1 * int2

from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/003.txt") as file:
    data = file.read()
    tot = 0
    enabled = True
    for i in range(len(data)):
        ret = check_slice(data[i:])
        if ret == True or ret == False:
            enabled = ret
        elif enabled and ret != None:
            tot += ret
    print(tot)


