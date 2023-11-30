# 714. Best Time to Buy and Sell Stock with Transaction Fee

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        dp = [[0] * n for _ in range(2)]
        # dp[0][i] max profit buy up till day i
        # dp[1][i] max profit sell up till day i

        dp[0][0] = -prices[0] - fee
        
        for i in range(1, n):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] - prices[i] - fee)
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + prices[i])
        
        return max(dp[1][n-1], dp[0][n-1])
    