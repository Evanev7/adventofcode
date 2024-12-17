from pathlib import Path

with open(f"{Path(__file__).parent.resolve()}/017.txt") as file:
    data = file.read().strip()

    reg_a, reg_b, reg_c, _, instrs = data.split("\n")
    reg_a = int(reg_a.split(": ")[1])
    reg_b = int(reg_b.split(": ")[1])
    reg_c = int(reg_c.split(": ")[1])
    instrs = [int(i) for i in instrs.split(": ")[1].split(",")]
    instr_ptr = 0

    reg_a = 7474474103313322340

    out = []
    while True:
        if instr_ptr >= len(instrs):
            break
        opcode, operand = instrs[instr_ptr], instrs[instr_ptr+1]
        if opcode in {0,2,5,6,7}:
            # combo -> literal conversion
            match operand:
                case 4:
                    operand = reg_a
                case 5:
                    operand = reg_b
                case 6:
                    operand = reg_c
                case 7:
                    raise ValueError
        match opcode:
            # adv
            case 0:
                reg_a = reg_a // 2**operand
                instr_ptr += 2
            # bxl
            case 1:
                reg_b = reg_b ^ operand
                instr_ptr += 2
            # bst
            case 2:
                reg_b = operand % 8
                instr_ptr += 2
            # jnz
            case 3:
                if reg_a != 0:
                    instr_ptr = operand
                else:
                    instr_ptr += 2
            # bxc
            case 4:
                reg_b = reg_b ^ reg_c
                instr_ptr += 2
            # out
            case 5:
                out.append(str(operand % 8))
                instr_ptr += 2
            # bdv
            case 6:
                reg_b = reg_a // 2**operand
                instr_ptr += 2
            # cdv
            case 7:
                reg_c = reg_a // 2**operand
                instr_ptr += 2
    print(",".join(out))