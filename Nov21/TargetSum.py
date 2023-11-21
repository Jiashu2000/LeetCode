# 494. Target Sum

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        if tot < abs(target):
            return 0
        t = (tot - target) // 2
        if (tot - target)%2 == 1:
            return 0

        dp = [0] * (t + 1)
        dp[0] = 1

        for num in nums:
            for j in range(t, num-1, -1):
                dp[j] += dp[j - num]
        
        return dp[t]