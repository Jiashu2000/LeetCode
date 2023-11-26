# 213. House Robber II

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return nums[0]
        if n <= 2:
            return max(nums[0], nums[1])

        dp = nums[:]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n-1): 
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        cur_max = dp[n-2]

        dp = nums[:]
        dp[2] = max(nums[1], nums[2])
        for i in range(3, n): 
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        cur_max = max(cur_max, dp[n-1])

        return cur_max