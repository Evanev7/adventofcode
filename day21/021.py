numpad = {
    "7": (0,0),
    "8": (1,0),
    "9": (2,0),
    "4": (0,1),
    "5": (1,1),
    "6": (2,1),
    "1": (0,2),
    "2": (1,2),
    "3": (2,2),
    "0": (1,3),
    "A": (2,3)
}
keypad = {
    "^": (1,0),
    "A": (2,0),
    "<": (0,1),
    "v": (1,1),
    ">": (2,1),
}
keypad_moves = {
    'AA':['AA'],
    'A^':['A<', '<A'],
    'Av':['A<', '<v', 'vA'],
    'A>':['Av', 'vA'],
        # v<<A
    'A<':['Av', 'v<', '<<' , '<A'],
    '^A':['A>', '>A'],
    '^^':['AA'],
    '^v':['Av', 'vA'],
    '^>':['Av', 'v>', '>A'],
    '^<':['Av', 'v<', '<A'],
    'vA':['A^', '^>', '>A'],
    'v^':['A^', '^A'],
    'vv':['AA'],
    'v>':['A>', '>A'],
    'v<':['A<', '<A'],
    '>A':['A^', '^A'],
    '>^':['A<', '<^', '^A'],
    '>v':['A<', '<A'],
    '>>':['AA'],
    '><':['A<', '<<', '<A'],
    '<A':['A>', '>>', '>^', '^A'],
    '<^':['A>', '>^', '^A'],
    '<v':['A>', '>A'],
    '<>':['A>', '>>', '>A'],
    '<<':['AA'],
}

def dir_to_string(pos, target):
    # if we need to dodge the gap
    offs = (target[0] - pos[0], target[1] - pos[1])
    if (pos[1] == 3 and target[0] == 0):
        return "^" * -offs[1] + "<" * -offs[0] + "A"
    if ((pos[0] == 0) and target[1] == 3):
        return ">" * offs[1] + "v" * offs[0] + "A"

    return ("<" * abs(offs[0]) if offs[0] < 0 else "") + ("^" * abs(offs[1]) if offs[1] < 0 else "") + ("v" * abs(offs[1]) if offs[1] > 0 else "") + (">" * abs(offs[0]) if offs[0] > 0 else "") + "A"

def get_numpad(string):
    pos = numpad["A"]
    out = ""
    for char in string:
        out += dir_to_string(pos, numpad[char])
        pos = numpad[char]
    return out

def string_to_states(s):
    start = "A"
    out = dict()
    for char in s:
        subj = start + char
        if subj not in out.keys():
            out[subj] = 1
        else:
            out[subj] += 1
        start = char
    return out

def iterate(keypresses):
    out = dict()
    #shouldbematrixshouldbematrixshouldbematrix
    for k,v in keypresses.items():
        for i in keypad_moves[k]:
            if i not in out.keys():
                out[i] = v
            else:
                out[i] += v
    return out

# I miss the indentation ok
if __name__ == "__main__":
    data = """169A
279A
540A
869A
789A"""
    tot = 0
    for row in data.split("\n"):
        init = string_to_states(get_numpad(row))
        num_itrs = 25
        for _ in range(num_itrs):
            init = iterate(init)
        tot += (int(row[:3]) * sum(init.values()))
    print(tot)