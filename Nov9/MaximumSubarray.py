# 53. Maximum Subarray

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = float("-inf")
        presum = 0
        for num in nums:
            presum = max(num, presum + num)
            if presum > maxsum:
                maxsum = presum
        return maxsum

'''
time: o(n)
space: o(1)
'''