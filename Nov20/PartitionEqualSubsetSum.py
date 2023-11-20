# 416.Partition Equal Subset Sum

from typing import List

class Solution:
    def __init__(self):
        self.dp = []
        self.cur_sum = 0

    def canPartition(self, nums: List[int]) -> bool:
        tot = sum(nums)
        if tot%2 == 1:
            return False
        target = tot//2
        n = len(nums)
        nums.sort()
        used = [0] * n
        for i in range(n):
            self.dp.append(set())
        return self.backtrack(nums, 0, target, used)
    
    def backtrack(self, nums, idx, target, used):
        if self.cur_sum >= target:
            if self.cur_sum == target:
                return True
            return False
        
        if idx >= len(nums) or self.cur_sum in self.dp[idx]:
            return False
        
        for i in range(idx, len(nums)):
            if i > 0 and nums[i-1] == nums[i] and used[i-1] == 0:
                continue
            self.cur_sum += nums[i]
            used[i] = 1
            if self.backtrack(nums, i + 1, target, used):
                return True
            self.cur_sum -= nums[i]
            used[i] = 0
        
        self.dp[idx].add(self.cur_sum)
        return False


    def canPartition_dp(self, nums: List[int]) -> bool:
        n = len(nums)
        tot = sum(nums)
        if tot % 2 == 1:
            return False
        target = tot//2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for i in range(n):
            for j in range(target, -1, -1):
                if j >= nums[i]:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[target] 