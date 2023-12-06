# 496. Next Greater Element I

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums2)
        next = [-1] * n
        stack = []
        dp = dict()
        for i in range(n):
            cur = nums2[i]
            if len(stack) == 0 or cur <= nums2[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and cur > nums2[stack[-1]]:
                    idx = stack.pop()
                    next[idx] = cur
                    dp[nums2[idx]] = next[idx]
                stack.append(i)
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in dp:
                ans[i] = dp[nums1[i]]
        return ans