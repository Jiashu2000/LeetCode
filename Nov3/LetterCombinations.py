# 17. Letter Combinations of a Phone Number

from typing import List

class Solution:

    def __init__(self) -> None:
        self.list = []
        self.res = []
        self.dict = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.backtrack(digits, 0)
        return self.res

    def backtrack(self, digits, idx):
        if len(self.list) == len(digits):
            self.res.append(''.join(self.list))
            return
        num = int(digits[idx])
        for i in range(len(self.dict[num])):
            self.list.append(self.dict[num][i])
            self.backtrack(digits, idx+1)
            self.list.pop()        

'''
time: o(n * 4^n)
space: o(n * 4^n)
'''