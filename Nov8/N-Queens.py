# 51. N-Queens

from typing import List

class Solution:

    def __init__(self) -> None:
        self.board = None
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.'] * n for _ in range(n)]
        self.backtrack(n, 0)
        return self.res

    def backtrack(self, n, row):
        if row == n:
            l = []
            for b in self.board:
                l.append(''.join(b))
            self.res.append(l)

        for c in range(n):
            if self.isValid(row, c, n):
                self.board[row][c] = 'Q'
                self.backtrack(n, row+1)
                self.board[row][c] = '.'
    
    def isValid(self, row, col, n):
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False
        
        for i in range(1, row+1):
            nr = row - i
            nc = col - i
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if self.board[nr][nc] == 'Q':
                return False
        
        for i in range(1, row+1):
            nr = row - i
            nc = col + i
            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue
            if self.board[nr][nc] == 'Q':
                return False  

        return True   
    
'''
time: o(n!)
space: o(n^2)
'''