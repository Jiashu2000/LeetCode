# 518. Coin Change II

from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0] * (amount+1)
        dp[0] = 1
        for j in range(n):
            c = coins[j]
            for i in range(amount+1):
                if i >= c and dp[i-c] >= 1:
                    dp[i] += dp[i-c]
        return dp[amount]

'''
如果求组合数就是外层for循环遍历物品, 内层for遍历背包。

如果求排列数就是外层for遍历背包, 内层for循环遍历物品。

'''