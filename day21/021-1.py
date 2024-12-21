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

def input_length(string):
    pos = keypad["A"]
    tot = 0
    for char in string:
        tot += abs(pos[0] - keypad[char][0]) + abs(pos[1] - keypad[char][1]) + 1
        pos = keypad[char]
    return tot

def first_to_string():
    offset = (target[0] - pos[0], target[1] - pos[1])
    parts = (("<" if offset[0] < 0 else ">") * abs(offset[0]), ("v" if offset[1] > 0 else "^") * abs(offset[1]))
    if parts[0] == "":
        return [parts[1] + "A"]
    elif parts[1] == "":
        return [parts[0] + "A"]
    else:
        opt1 = parts[0] + parts[1] + "A"
        opt2 = parts[1] + parts[0] + "A"
        return [opt1, opt2]

def second_to_string():
    offset = (target[0] - pos[0], target[1] - pos[1])
    parts = (("<" if offset[0] < 0 else ">") * abs(offset[0]), ("v" if offset[1] > 0 else "^") * abs(offset[1]))
    if parts[0] == "":
        return parts[1] + "A"
    elif parts[1] == "":
        return parts[0] + "A"
    else:
        opt1 = parts[0] + parts[1] + "A"
        opt2 = parts[1] + parts[0] + "A"
        if input_length(opt1) > input_length(opt2):
            return opt1
        else:
            return opt2

def third_to_string():
    offset = (target[0] - pos[0], target[1] - pos[1])
    parts = (("<" if offset[0] < 0 else ">") * abs(offset[0]), ("v" if offset[1] > 0 else "^") * abs(offset[1]))
    if parts[0] == "":
        return parts[1] + "A"
    elif parts[1] == "":
        return parts[0] + "A"
    else:
        return parts[0] + parts[1] + "A"
        


def dir_to_string(pos, target, depth):
    offset = (target[0] - pos[0], target[1] - pos[1])
    parts = (("<" if offset[0] < 0 else ">") * abs(offset[0]), ("v" if offset[1] > 0 else "^") * abs(offset[1]))
    if parts[0] == "":
        return parts[1] + "A"
    elif parts[1] == "":
        return parts[0] + "A"
    else:
        opt1 = parts[0] + parts[1] + "A"
        opt2 = parts[1] + parts[0] + "A"
        if input_length(opt1) > input_length(opt2):
            return opt1
        else:
            return opt2

def evaluate_string(pad, string, depth):
    options = dir_to_string(pad["A"], pad[string[0]], depth)
    for i in range(len(string)-1):
        options += dir_to_string(pad[string[i]], pad[string[i+1]], depth)
    return options


# I miss the indentation ok
if __name__ == "__main__":
    data = """379A"""
    print(input_length(">>A^A"))
    tot = 0
    for ask in data.split("\n"):
        print(ask)
        out = evaluate_string(keypad, evaluate_string(keypad, evaluate_string(numpad, ask, 0), 1), 2) 
        tot += len(out) * int(ask[:3])
        print(len(out), int(ask[:3]))
    print(tot)