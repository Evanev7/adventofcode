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
basis = {
    'AA':0,
    'A^':1,
    'Av':2,
    'A>':3,
    'A<':4,
    '^A':5,
    '^^':6,
    '^v':7,
    '^>':8,
    '^<':9,
    'vA':10,
    'v^':11,
    'vv':12,
    'v>':13,
    'v<':14,
    '>A':15,
    '>^':16,
    '>v':17,
    '>>':18,
    '><':19,
    '<A':20,
    '<^':21,
    '<v':22,
    '<>':23,
    '<<':24,
}

def unbasis(i):
    for k,v in basis.items():
        if v == i:
            return k
    return ""

class KeypadMatrix:
    def __init__(self, preinit = None):
        if preinit != None:
            self.matrix = preinit
            return
        self.matrix = [[0 for width in range(25)] for height in range(25)]
        # basis is {^^, ^>, ^v, .., A<, AA}.
        for k in keypad_moves.keys():
            vec = [0 for _ in range(25)]
            for state in keypad_moves[k]:
                vec[basis[state]] += 1
            self.matrix[basis[k]] = vec

    def __mul__(self, other):
        result = [[0 for j in range(len(other.matrix[i]))] for i in range(len(self.matrix))]
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self.matrix[i][k] * other.matrix[k][j]
        return KeypadMatrix(result)
    
    def __pow__(self, other):
        out = self
        for i in range(other-1):
            out *= self
        return out
    
    def __str__(self):
        return "\n".join([str(i) for i in self.matrix])
    
    def sum_items(self):
        tot = 0
        for i in self.matrix:
            for j in i:
                tot += j
        return tot
    
    def debug_states(self):
        return (" ".join([unbasis(i) * j[0] for i,j in enumerate(self.matrix)]))

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
    out = []
    for char in s:
        out.append(start + char)
        start = char
    return out

def state_to_vec(s):
    vec = [[0] for i in range(25)]
    for state in s:
        vec[basis[state]][0] += 1
    return KeypadMatrix(vec)

# I miss the indentation ok
if __name__ == "__main__":
    print("A^v><")
    data = """029A"""
    print(get_numpad(data))
    k = KeypadMatrix()
    s = "vA"
    # vA -> Av vA -> A< <v vA A^ ^> >A
    print(state_to_vec(string_to_states(s)).debug_states())
    print((k * state_to_vec(string_to_states(s))).matrix)
    print((k * state_to_vec(string_to_states(s))).debug_states())
    print((k * state_to_vec(string_to_states(s))).sum_items())
    for string in data.split("\n"):
        numpad = get_numpad(string)
        print(numpad)
        print((k**2 * state_to_vec(string_to_states(s))).matrix)
        print((k**3 * state_to_vec(string_to_states(s))).sum_items())