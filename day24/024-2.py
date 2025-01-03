from pathlib import Path

def get(val, dependencies, state):
    if val in state.keys():
        return state[val]
    a, b, op = dependencies[val]
    a = get(a, dependencies, state)
    b = get(b, dependencies, state)
    match op:
        case "OR":
            return a or b
        case "AND":
            return a and b
        case "XOR":
            return a ^ b

def ev(f, dependencies, state):
    tot = 0
    ctr = 0
    while f"{f}{ctr:02}" in dependencies.keys() or f"{f}{ctr:02}" in state.keys():
        if get(f"{f}{ctr:02}", dependencies, state):
            tot += 2 ** ctr 
        ctr += 1
    return tot

def swap_dependencies(a, b, dependencies):
    dependencies[a], dependencies[b] = dependencies[b], dependencies[a]

with open(f"{Path(__file__).parent.resolve()}/024.txt") as file:
    data = file.read().strip()

    inputs, instringtions = data.split("\n\n")
    state = dict()
    for row in inputs.split("\n"):
        wire, wire_state = row.split(": ")
        state[wire] = bool(int(wire_state))
    dependencies = dict()
    for row in instringtions.split("\n"):
        parts = row.split(" ")
        dependencies[parts[4]] = (parts[0], parts[2], parts[1])
    for i in range(45):
        state[f"x{i:02}"] = True
        state[f"y{i:02}"] = True

    # A three bit adder on A B C is
    # (A XOR B) XOR C, with carry (A XOR B) AND C or A and B (or (A and B) or (A and C) or (B and C)) - these are equivalent
    # We see z22 = y22 AND x22 - it should be ??1 XOR ??2 where (lets say) ??1 = x22 XOR y22 = cdf, and cdf XOR cmn = hwq, so hwq <-> z22
    # We see z29 = rpq OR grd - should be XOR. x29 XOR y29 is bfq, bfq XOR dcf is gbs - should be z29.
    # Remaining problems are with the carry bits.
    # Checking |z-x-y|, we see log2|z-x-y| = 14 - so there's an issue around z14
    # We see z14 = hgw XOR wss. hgw = cmd OR vns, wss = x14 AND y14. wss should feed into an OR gate not an XOR gate, so we should swap with wrm = x14 XOR y14

    # At this stage, we correctly add our given inputs, but we need to be able to add any inputs. 
    # Let's try another input state - all 1s. We see an input at 256, so z08
    # We see z08 = vqp AND frr, vqp = x08 XOR y08 and thm = vqp XOR frr so we need to swap z08 with thm

    swap_dependencies("z22", "hwq", dependencies)
    swap_dependencies("z29", "gbs", dependencies)
    swap_dependencies("wrm", "wss", dependencies)
    swap_dependencies("z08", "thm", dependencies)

    x = ev("x", dependencies, state)
    y = ev("y", dependencies, state)
    z = ev("z", dependencies, state)

    swappers = ["z22", "hwq", "z29", "gbs", "wrm", "wss", "z08", "thm"]
    print(",".join(sorted(swappers)))