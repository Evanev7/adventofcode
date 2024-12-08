from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/007.txt") as file:
    data = file.read().strip()
    
    tot = 0
    for eqn in data.split("\n"):
        tv = int(eqn.split(":")[0])
        ints = [int(i) for i in eqn.split(":")[1].strip().split(" ")]
        # Let's just enumerate the possibilities.
        for i in range(2**(len(ints)-1)):
            testints = ints.copy()[::-1]
            opts = i
            accum = testints.pop()
            while testints != []:
                if opts % 2 == 0:
                    accum += testints.pop()
                else:
                    accum *= testints.pop()
                opts //= 2
                if accum > tv:
                    break
            if accum == tv:
                tot += tv
                break
        
        
    print(tot)

