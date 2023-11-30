# 309. Best Time to Buy and Sell Stock with Cooldown

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        if n == 2:
            if prices[1] > prices[0]:
                return prices[1] - prices[0]
            return 0
        
        dp = [[0] * n for _ in range(3)]
        # buy on the first day
        # dp[0][i] max profit up to day i if you have a stock.
        # dp[1][i] max profit up to day i if you sold stock on the day
        # dp[2][i] max profit up to day i if do not have a stock.  (exclude cooldown)
        dp[0][0] = -prices[0]
        dp[0][1] = max(-prices[0], -prices[1])

        dp[1][1] = prices[1] + dp[0][0]
        dp[2][1] = dp[1][0]
        
        for i in range(2, n):
            dp[0][i] = max(dp[0][i-1], dp[2][i-1] - prices[i])
            dp[1][i] = dp[0][i-1] + prices[i]
            dp[2][i] = max(dp[2][i-1], dp[1][i-1])
        
        ans = 0
        for i in range(3):
            ans = max(ans, dp[i][n-1])
        
        return ans


        