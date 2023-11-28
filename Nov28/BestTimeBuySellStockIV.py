# 188. Best Time to Buy and Sell Stock IV

from tying import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * (2 * k) for i in range(2)]
        for i in range(2 * k):
            if i % 2 == 0:
                dp[0][i] = -prices[0]
            else:
                dp[0][i] = 0

        for i in range(1, n):
            for j in range(2 * k):
                if j == 0:
                    dp[1][j] = max(dp[0][j], -prices[i])
                elif j % 2 == 1:
                    dp[1][j] = max(dp[0][j], prices[i] + dp[0][j-1])
                elif j % 2 == 0:
                    dp[1][j] = max(dp[0][j], dp[0][j-1] - prices[i])
            dp[0] = dp[1]
        return dp[1][2 * k-1]