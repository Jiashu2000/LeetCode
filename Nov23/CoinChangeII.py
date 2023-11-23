# 518 Coin Change II

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        n = len(coins)
        for i in range(n):
            c = coins[i]
            for j in range(amount+1):
                if j >= c:
                    dp[j] += dp[j-c]
        return dp[amount]

'''
排列背包放在外
组合物品放在外
'''