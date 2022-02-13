import math
import re



class Solution:

    def __init__(self, board):
        self.board = board;

    def solve(self):
        self.solveSudoku(self.board)
        print(self.board)

    def get_empty(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    return (i, j)

        return ()

    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        empty = self.get_empty(board)

        if empty == ():
            return True
        
        i, j = empty
        
        for num in range(1, 10):
            if self.is_good(board, i, j, str(num)):
                board[i][j] = str(num)
                if self.solveSudoku(board):
                    return True
                board[i][j] = '.'

                            
    def is_good(self, board, row, col, num):
        return self.row_good(board, row, num) and \
            self.col_good(board, col, num) and self.square_good(board, row, col, num)
        
    def row_good(self, board, row, num):
        for a in board[row]:
            if a == num:
                return False
        return True
         
    
    def col_good(self, board, col, num):
        for row in board:
            if row[col] == num:
                return False
        return True
        
    def square_good(self, board, row, col, item):
        bottom, top = math.floor(row/3)*3, math.floor(row/3)*3 + 3;
        left, right = math.floor(col/3)*3, math.floor(col/3)*3 + 3;
        print(bottom, top)
        
        for i in range(bottom, top):
            for j in range(left, right):
                if board[i][j] == item:
                    return False
                
        return True

board = [["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

s = Solution(board)
# print(s.square_good(board, 3, 3,'8'))
s.solve()