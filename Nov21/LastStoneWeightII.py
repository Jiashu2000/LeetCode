# 1049. Last Stone Weight II

from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        n = len(stones)
        
        tot = sum(stones)
        target = tot//2
        dp = [0] * (target + 1)

        for i in range(n):
            s = stones[i]
            for j in range(target, s-1, -1):
                dp[j] = max(dp[j], dp[j - s] + s)

        return (tot - dp[target]) - dp[target]

'''
transform the stone canceling problem to
the adding problem
'''