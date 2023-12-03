
from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_len = 1
        n = len(nums)
        i = 1
        curlen = 1
        while i < n:
            curlen = 1
            while i < n and nums[i] > nums[i-1]:
                curlen += 1
                i += 1
            i += 1
            max_len = max(max_len, curlen)
        return max_len
        
            