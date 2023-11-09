# 376. Wiggle Subsequence

from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        prediff = 0
        curdiff = 0
        res = 1
        for i in range(n-1):
            curdiff = nums[i+1] - nums[i]
            if (prediff >= 0 and curdiff < 0) or (prediff <= 0 and curdiff > 0):
                res += 1
                prediff = curdiff
        return res

'''
time: o(n)
space: o(1)
'''