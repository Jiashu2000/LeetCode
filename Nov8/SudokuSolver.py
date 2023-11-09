# 37. Sudoku Solver

from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)
        return 
    


    def backtrack(self, board):
        n = len(board)
        for i in range(n):
            for j in range(n):
                if board[i][j] != '.':
                    continue
                for k in range(1, 10):
                    if self.isValid(str(k), i, j, board):
                        board[i][j] = str(k)
                        if self.backtrack(board):
                            return True
                        board[i][j] = '.'
                return False
        return True
    

    def isValid(self, k, i, j, board):
        n = len(board)
        for m in range(n):
            if board[m][j] == k:
                return False
            if board[i][m] == k: 
                return False
        
        startx = i//3 * 3
        starty = j//3 * 3
        
        for r in range(startx, startx+3):
            for c in range(starty, starty+3):
                if board[r][c] == k:
                    return False
        return True