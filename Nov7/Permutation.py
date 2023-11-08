# 46. Permutation

from typing import List

class Solution:

    def __init__(self) -> None:
        self.res = []
        self.list = [] 

    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False] * len(nums)
        self.backtrack(nums, used)
        return self.res
    

    def backtrack(self, nums, used):
        if len(self.list) == len(nums):
            self.res.append(self.list[:])
            return
        for i in range(0, len(nums)):
            if not used[i]:
                used[i] = True 
                self.list.append(nums[i])
                self.backtrack(nums, used)
                used[i] = False
                self.list.pop()


'''
time: o(n!)
space: o(n)
'''
        

  