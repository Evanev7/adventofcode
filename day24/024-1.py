from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/024.txt") as file:
    data = file.read().strip()
    #data = \
    """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

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