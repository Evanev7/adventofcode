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

def dir_to_string(pos, target):
    offset = (target[0] - pos[0], target[1] - pos[1])
    parts = (("<" if offset[0] < 0 else ">") * abs(offset[0]), ("v" if offset[1] > 0 else "^") * abs(offset[1]))
    if parts[0] == "":
        return [parts[1] + "A"]
    elif parts[1] == "":
        return [parts[0] + "A"]
    else:
        return [parts[0] + parts[1] + "A", parts[1] + parts[0] + "A"]

def ir(pos, target):
    o = dir_to_string(pos, target)
    if len(o) == 1:
        return o[0]
    else:
        a, b = o
        if strlen(a) > strlen(b):
            return a
        else:
            return b

def get_all_numpads(string):
    pos = numpad["A"]
    out = [""]
    for char in string:
        out = [i + j for i in out for j in dir_to_string(pos, numpad[char])]
        pos = numpad[char]
    return out

def strlen(string):
    tot = 0
    for i in range(len(string)-1):
        start_pos = keypad[string[i]]
        end_pos = keypad[string[i+1]]
        tot += abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])
    return tot

def to_vec(string):
    undir = {"^":0, ">":1, "v":2, "<":3, "A": 4}
    out = [0 for i in range(25)]
    string = "A" + string
    for j in range(len(string) - 1):
        ind = undir[string[j]] * 5 + undir[string[j+1]]
        out[ind] += 1
    return out

def vec_to_mat(vec):
    return KeypadMatrix([[i] for i in vec])

class KeypadMatrix:
    def __init__(self, preinit = None):
        if preinit != None:
            self.matrix = preinit
            return
        # The relevant state transitions are the ordered pairs of ^>v<A
        self.matrix = [[0 for width in range(25)] for height in range(25)]
        dirs = ["^", ">", "v", "<", "A"]
        # basis is {^^, ^>, ^v, .., A<, AA}.
        for i in range(25):
            from_char = dirs[i // 5]
            to_char = dirs[i % 5]
            start_pos = keypad[from_char]
            end_pos = keypad[to_char]
            inputs = ir(start_pos, end_pos)
            # let V = (^|v|<|>) 
            # inputs here is a string V*A. We're gonna interpret this as a (VV)*(VA)
            # The edge case is a single A, which gets mapped to AA.
            # For example, >vA -> A> >A Av vA AA. 
            self.matrix[i] = to_vec(inputs)

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

# I miss the indentation ok
if __name__ == "__main__":
    data = """029A"""
    for numpad in get_all_numpads(data):
        print(numpad)
        print(KeypadMatrix() * vec_to_mat(to_vec(numpad)))
        print((KeypadMatrix()**2 * vec_to_mat(to_vec(numpad))).sum_items())