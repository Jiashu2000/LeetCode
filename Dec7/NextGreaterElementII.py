# 503. Next Greater Element II

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.extend(nums)
        ans = [-1] * n
        stack = []
        for i in range(2 * n):
            i = i%n

            cur = nums[i]
            if len(stack) == 0 or cur <= nums[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and cur > nums[stack[-1]]:
                    idx = stack.pop()
                    if ans[idx] == -1:
                        ans[idx] = cur
                stack.append(i)
        return ans