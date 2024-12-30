from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/024.txt") as file:
    data = file.read().strip()

    inputs, instringtions = data.split("\n\n")
    state = dict()
    for row in inputs.split("\n"):
        wire, wire_state = row.split(": ")
        state[wire] = bool(int(wire_state))
    instructions = dict()
    for row in instringtions.split("\n"):
        parts = row.split(" ")
        if (parts[0], parts[2]) not in instructions.keys():
            instructions[(parts[0], parts[2])] = set([(parts[1], parts[4])])
        else:
            instructions[(parts[0], parts[2])].add((parts[1], parts[4]))


    while instructions != dict():
        for s1, s2 in instructions.keys():
            if s1 in state.keys() and s2 in state.keys():
                for instruction, target in instructions[(s1, s2)]:
                    if target in state.keys():
                        continue
                    print(f"{s1} {instruction} {s2} -> {target} ")
                    match instruction:
                        case "AND":
                            state[target] = state[s1] and state[s2]
                        case "OR":
                            state[target] = state[s1] or state[s2]
                        case "XOR":
                            state[target] = state[s1] ^ state[s2]
                del instructions[(s1,s2)]
                break 
    
    tot = 0
    ctr = 0
    while f"z{ctr:02}" in state.keys():
        tot += 2 ** ctr * state[f"z{ctr:02}"]
        ctr += 1
    print(f"{tot}")