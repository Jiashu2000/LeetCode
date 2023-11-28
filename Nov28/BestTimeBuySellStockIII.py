# 123. Best Time to Buy and Sell Stock III

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * n for i in range(4)]
        dp[0][0] = -prices[0]
        dp[2][0] = float("-inf")
        
        for i in range(1, n):
            dp[0][i] = max(-prices[i], dp[0][i-1])
            dp[1][i] = max(dp[1][i-1], prices[i] + dp[0][i-1])
            dp[2][i] = max(dp[2][i-1], dp[1][i-1] - prices[i])
            dp[3][i] = max(dp[3][i-1], prices[i] + dp[2][i-1])
        
        res = float("-inf")
        for i in range(4):
            res = max(res, dp[i][n-1])
        return res