import copy
filename = 'puzzle.txt'
def parse_puzzle(file):
    f = open(file, 'r')
    lines = f.readlines()
    res = []
    for line in lines:
        newline = []
        for ch in line:
            if ch == '\n':
                continue
            if ch == 'X':
                newline.append(0)
            else:
                newline.append(int(ch))
        res.append(newline)
    return res
