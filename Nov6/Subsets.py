# 78. Subsets

from typing import List

class Solution:

    def __init__(self) -> None:
        self.res = []
        self.list = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, idx):
        self.res.append(self.list[:])
        
        for i in range(idx, len(nums)):
            self.list.append(nums[i])
            self.backtrack(nums, i+1)
            self.list.pop()

'''
time:
    O(n * 2^n)
    there are n numbers and two decisions (include/ leave)
space:
    O(n)
'''
        
  