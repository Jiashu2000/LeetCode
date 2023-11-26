# 198. House Robber

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[n-1]

    def rob_2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        first = nums[0]
        second = max(nums[0], nums[1])

        for i in range(2, n):
            cur_max = max(first + nums[i], second)
            first = second
            second = cur_max
        return second