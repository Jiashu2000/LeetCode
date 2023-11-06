# 90. Subsets II

from typing import List

class Solution:

    def __init__(self) -> None:
        self.res = []
        self.list = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        used = [False] * len(nums)
        self.backtrack(nums, 0, used)
        return self.res

    def backtrack(self, nums, idx, used):
        self.res.append(self.list[:])
        
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1] and not used[i]:
                continue
            self.list.append(nums[i])
            used[i] = True
            self.backtrack(nums, i+1, used)
            self.list.pop()
            used[i] = False

'''
time:
    o(2^n)
space:
    o(n)

the total number of nodes for a tree of depth L is (N^(L+1)-1) / (N-1)
where L is the depth and N is the number of subnodes
'''
