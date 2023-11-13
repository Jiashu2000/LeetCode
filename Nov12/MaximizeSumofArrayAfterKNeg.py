# 1005. Maximize Sum of Array After K Negations

from typing import List

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i = 0
        # deal with negative nums
        while i < len(nums) and nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        
        k = k%2

        if k > 0:
            if i > 0 and i <= len(nums) - 1 and nums[i] > nums[i-1]:
                nums[i-1] = - nums[i-1]
            elif i > 0 and i <= len(nums) - 1 and nums[i] <= nums[i-1]:
                nums[i] = - nums[i]
            elif i == 0:
                nums[i] = -nums[i]
            elif i == len(nums):
                i -= 1
                nums[i] = - nums[i]
                
        return sum(nums)
