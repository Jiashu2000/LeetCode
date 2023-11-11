# 45. Jump Game II

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        curdist = 0
        nextdist = 0
        res = 0
        for i in range(n):
            nextdist = max(nextdist, i+nums[i])
            if i == curdist:
                curdist = nextdist
                res += 1
                if nextdist >= n - 1:
                    break
        return res
    

'''
time: o(n)
space: o(1)
'''