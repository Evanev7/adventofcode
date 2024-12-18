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

def sim(reg_a):
    out = []
    while reg_a > 0:
        out.append(f(reg_a))
        reg_a //= 8
    return out


with open(f"{Path(__file__).parent.resolve()}/017.txt") as file:
    data = file.read().strip()

    instrs = data.split("\n\n")[1]
    instrs = [int(i) for i in instrs.split(": ")[1].split(",")]

    a_opts = set([0])

    flag = True
    while flag:
        new_a = set()
        for opt in a_opts:
            for i in range(8):
                produces = sim(opt * 8 + i)
                if produces == instrs[-len(produces):]:
                    new_a.add(opt * 8 + i)
                if produces == instrs:
                    flag = False
        a_opts = new_a
    print(min(a_opts))
    





# ###PROGRAM###
# b-store     A # B = A % 8
# b-xor-lit   7 # B = 7 ^ (A % 8)
# c-div       B # C = A // 2 ** (7 ^ (A % 8))
# b-xor-c     1 # B = 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8)))
# b-xor-lit   4 # B = 4 ^ 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8)))
# out         B # print(4 ^ 7 ^ (A % 8) ^ (A // 2 ** (7 ^ (A % 8))))
# a-div       3 # A // 8
# jump-nzero  0 # loop