# 55. Jump Game

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        i = 0
        while i <= min(reach, len(nums)-1):
            steps  = nums[i]
            reach = max(reach, i + steps)
            if reach >= len(nums) -1:
                return  True
            i += 1
        return False

'''
time: o(n)
space: o(1)
'''