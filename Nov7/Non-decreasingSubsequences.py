# 491. Non-decreasing Subsequences

from typing import List

class Solution:

    def __init__(self) -> None:
        self.res = []
        self.list = [] 

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, idx):
        if len(self.list) >= 2:
            self.res.append(self.list[:])
        used = set()
        for i in range(idx, len(nums)):
            if len(self.list) > 0 and nums[i] < self.list[-1]:
                continue
            if nums[i] in used:
                continue
            used.add(nums[i])
            self.list.append(nums[i])
            self.backtrack(nums, i+1)
            self.list.pop()  

'''
time complexity:
    O(2^N)
space complexity:
    O(N)

同一父节点下的同层使用过的元素就不能再使用了
'''