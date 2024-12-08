from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/007.txt") as file:
    data = file.read().strip()
    """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    
    tot = 0
    import time
    now = time.time()
    for ind, eqn in enumerate(data.split("\n")):
        print(f"\rEquation {ind}/{len(data.split("\n"))}", end = "")
        tv = int(eqn.split(":")[0])
        ints = [int(i) for i in eqn.split(":")[1].strip().split(" ")]
        # Let's just enumerate the possibilities.
        for i in range(3**(len(ints)-1)):
            testints = ints.copy()[::-1]
            opts = i
            accum = testints.pop()
            while testints != []:
                match opts % 3:
                    case 0:
                        accum += testints.pop()
                    case 1:
                        accum *= testints.pop()
                    case 2:
                        accum = int(str(accum) + str(testints.pop()))
                opts //= 3
                if accum > tv:
                    break
            if accum == tv:
                tot += tv
                break
        
    print()
    print(tot)
    print(time.time() - now, "seconds")

