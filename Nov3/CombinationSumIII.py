# 216. Combination Sum III

from typing import List


class Solution:

    def __init__(self):
        self.list = []
        self.tot = 0
        self.res = []
    
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(k, n, 1)
        return self.res

    def backtrack(self, k, n, idx):
        if len(self.list) == k:
            if self.tot == n:
                self.res.append(self.list[:])
            return 
        
        if self.tot + idx > n:
            return
        
        for i in range(idx, 10):
            self.tot += i
            self.list.append(i)
            self.backtrack(k, n, i+1)
            self.tot -= i
            self.list.pop()

'''
time: o(k * 9 ^ k)
space: o(k)
'''