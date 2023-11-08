# 47. Permutation II

from typing import List

class Solution:

    def __init__(self) -> None:
        self.res = []
        self.list = []


    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        self.backtrack(nums, used)
        return self.res

    def backtrack(self, nums, used):
        if len(self.list) == len(nums):
            self.res.append(self.list[:])
            return
        for i in range(0, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i-1] == False:
                continue
            if used[i]:
                continue
            self.list.append(nums[i])
            used[i] = True
            self.backtrack(nums, used)
            self.list.pop()
            used[i] = False

'''
time: o(n!)
space: o(n)
'''