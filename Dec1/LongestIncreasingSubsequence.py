# 300. Longest Increasing Subsequence

from typing import List

class Solution:

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        l = []
        for i in range(n):
            cur = nums[i]
            if len(l) == 0 or cur > l[-1]:
                l.append(cur)
            else:
                idx = self.findIdx(l, cur)
                l[idx] = cur
        return len(l)
    
    def findIdx(self, l, t):
        left = 0
        right = len(l) - 1
        while left <= right:
            mid = left + (right - left)//2
            if l[mid] == t:
                return mid
            elif l[mid] > t:
                right = mid - 1
            else:
                left = mid + 1
        return max(0, left)

