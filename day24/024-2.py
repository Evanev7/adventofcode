from pathlib import Path

def sim_instructions(state, instructions):
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
    return ev(state, "z")

def ev(state, f):
    tot = 0
    ctr = 0
    while f+f"{ctr:02}" in state.keys():
        tot += 2 ** ctr * state[f+f"{ctr:02}"]
        ctr += 1
    return tot

    
with open(f"{Path(__file__).parent.resolve()}/024.txt") as file:
    data = file.read().strip()

    inputs, instringtions = data.split("\n\n")
    state = dict()
    for row in inputs.split("\n"):
        wire, wire_state = row.split(": ")
        state[wire] = bool(int(wire_state))
    instructions = dict()
    dependencies = dict()
    for row in instringtions.split("\n"):
        parts = row.split(" ")
        if (parts[0], parts[2]) not in instructions.keys():
            instructions[(parts[0], parts[2])] = set([(parts[1], parts[4])])
        else:
            instructions[(parts[0], parts[2])].add((parts[1], parts[4]))
        deps = set()
        if "x" not in parts[0] and "y" not in parts[0]:
            deps.add(parts[0])
            if parts[0] in dependencies.keys():
                deps = deps.union(dependencies[parts[0]])

        if "x" not in parts[2] and "y" not in parts[2]:
            deps.add(parts[2])
            if parts[2] in dependencies.keys():
                deps = deps.union(dependencies[parts[2]])
        dependencies[parts[4]] = deps
    x = ev(state, "x")
    y = ev(state, "y")
    z = sim_instructions(state, instructions)
    print(x, y, z)
    print(z - (x + y))
    print(f"{z-x-y:b}")
    diff_bits = reversed([bool(int(i)) for i in f"{z-x-y:b}"])
    swap_opts = set()
    for i, bit in enumerate(diff_bits):
        if bit:
            swap_opts = swap_opts.union(dependencies[f"z{i:02}"])
    swap_opts = list(swap_opts)
    print(len(swap_opts))
    import random
    while True:
        swap_opts_copy = swap_opts.copy()
        a1,a2,b1,b2,c1,c2,d1,d2 = random.sample(swap_opts_copy, 8)