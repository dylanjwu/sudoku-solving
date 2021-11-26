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

squares = [(0, 2), (3, 5), (6, 8)]

def inColumn(k, board, i, j):
    return k in [board[c][j] for c in range(9)]

def inRow(k, board, i, j):
    return k in board[i]

def inSquare(k, board, square_i, square_j):
    for i in range(square_i[0], square_i[1]+1):
        for j in range(square_j[0], square_j[1]+1):
            if board[i][j] == k:
                return True
    return False

def backtrack(i, j, board):
    print("i: " + str(i), "j: " + str(j))
    print("board: " + str(board))
    if i == 9:
        print("RESULT: " + str(board))
        return

    for k in range(1, 10):
        # print(board)
        sq_i = ()
        sq_j = ()
        for rng in squares:
            if i >= rng[0] and i <= rng[1]:
                sq_i = rng
            if j >= rng[0] and j <= rng[1]:
                sq_j = rng
        conds = [inRow(k,board,i,j),
            inColumn(k,board,i,j),
            inSquare(k, board, sq_i, sq_j)]

        print("board: " + str(board))
        print(conds)
        print(k, i, j) 

        if any(conds):
            continue

        newBoard = copy.deepcopy(board)
        if board[i][j] == 0:
            newBoard[i][j] = k
        if j == 8:
            # print("increase i")
            backtrack(i+1, 0, newBoard)
        else: 
            backtrack(i, j+1, newBoard)


# board =[[0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0]] 

b = parse_puzzle(filename)
print(b)
print(backtrack(0, 0, b[:]))


def loop_thru(i,  j):
    print(i, j)
    if i == 9 and j == 9:
        return
    if j == 9:
        loop_thru(i+1, 0)
    else:
        loop_thru(i, j+1)

# loop_thru(0,0)
