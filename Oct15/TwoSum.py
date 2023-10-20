# 1. Two Sum

from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            num = nums[i]
            if target - num in dict.keys():
                return [dict[target-num], i]
            dict[num] = i
        return [-1, -1]
    

    '''
    time complexity: o(n)
    space complexity: o(n)
    '''