from pathlib import Path

# Express A in base 8.
# A = a0 + 8*a1 + 8^2*a2 + ...
# f(a):
# makes b = f(a0) < 8
# b = 7 ^ a0
# makes c = a // 2**b % 8 - so can only be affected by a0, a1, a2, a3. 8**3 = 2**9 > 2 ** 7, so at worst c = a // 2**7 = (a2 // 2 + 4 * a3) % 8
# Therefore f(a) = f(a0, a1, a2, a3).
# Search space is 8*8*8*8 = 4096
# returns 4 ^ b ^ (a // 2**b) % 8.

def f(a):
    return 3 ^ (a % 8) ^ ((a // 2 ** (7 ^ (a % 8))) % 8)

def str2b8(s):
    acc = 0
    for i, l in enumerate(s):
        acc += int(l) * 8**(len(s) - i-1)
    return acc

with open(f"{Path(__file__).parent.resolve()}/017.txt") as file:
    data = file.read().strip()

    instrs = data.split("\n\n")[1]
    instrs = [int(i) for i in instrs.split(": ")[1].split(",")]

    memo = [set() for i in range(8)]
    for i in range(8**4):
        memo[f(i)].add(f"{i // 8**3}{i // 8**2 % 8}{i // 8 % 8}{i % 8}")
        if (f(i) != f(str2b8(f"{i // 8**3}{i // 8**2 % 8}{i // 8 % 8}{i % 8}"))):
            print(i)
            print(f(i))
            print(f"{i // 8**3}{i // 8**2 % 8}{i // 8 % 8}{i % 8}")
            print(str2b8(f"{i // 8**3}{i // 8**2 % 8}{i // 8 % 8}{i % 8}"))
            quit()

    valids = dict((i,set([i + ":" + str(f(str2b8(i)))])) for i in memo[instrs[-1]])
    for instr in instrs[-2::-1]:
        top_of_valids = dict()
        for i in valids:
            if i[-3:] in top_of_valids.keys():
                top_of_valids[i[-3:]].add(i)
            else:
                top_of_valids[i[-3:]] = {i}
        
        new_valids = dict()
        for rest in memo[instr]:
            if rest[:3] in top_of_valids.keys():
                for valid in top_of_valids[rest[:3]]:
                    new_valids[valid + rest[-1]] = (*valids[valid], rest + ":" + str(f(str2b8(rest))))
        valids = new_valids
    print(valids)

    # This simulator is accurate, so f is definitely correct.
    print(f(2340))
    out = []
    a = 7474474103313322340
    while a > 0:
        out.append(str(f(a)))
        a //= 8
    print(",".join(out))
        
            
             
    # Here's the algo
    # We're keeping a set of valid base 8 digits, starting from the MSD. 
    # The MSD is processed last, so corresponds to the final instruction.
    





# ###PROGRAM###
# b-store     A # B = A % 8
# b-xor-lit   7 # B = 7 ^ (A % 8)
# c-div       B # C = A // 2 ** (7 ^ (A % 8))
# b-xor-c     1 # B = 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8)))
# b-xor-lit   4 # B = 4 ^ 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8)))
# out         B # print(4 ^ 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8))))
# a-div       3 # A // 8
# jump-nzero  0 # loop