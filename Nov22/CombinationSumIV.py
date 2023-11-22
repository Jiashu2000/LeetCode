# 377. Combination Sum IV

from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [0] * (target + 1)
        dp[0] = 1
        for j in range(target+1):
            for i in range(n):
                if j >= nums[i]:
                    dp[j] += dp[j-nums[i]]
        return dp[target]

'''
如果求组合数就是外层for循环遍历物品, 内层for遍历背包。

如果求排列数就是外层for遍历背包, 内层for循环遍历物品。
'''