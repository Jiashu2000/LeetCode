# 42. Trapping Rain Water

from typing import List

class Solution:
    # suffix, prefix
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftmax_arr = [0] * n
        rightmax_arr = [0] * n
        leftmax_arr[0] = height[0]
        rightmax_arr[n-1] = height[n-1]
        for i in range(1, n):
            leftmax_arr[i] = max(leftmax_arr[i-1], height[i])
        for i in range(n-2, -1, -1):
            rightmax_arr[i] = max(rightmax_arr[i+1], height[i])
        
        ans = 0
        for i in range(1, n-1):
            ans += min(leftmax_arr[i], rightmax_arr[i]) - height[i]
        return ans

    # atack
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        stack = []
        start = 0
        while start < n and height[start] == 0:
            start += 1
        for i in range(start, n):
            cur = height[i]
            if len(stack) == 0 or cur < height[stack[-1]]:
                stack.append(i)
            elif cur == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while len(stack) > 0 and cur >= height[stack[-1]]:
                    mid = stack.pop()
                    if len(stack) > 0:
                        left = stack[-1]
                        h = min(height[left], cur) - height[mid]
                        w = i - left - 1
                        ans += h * w
                stack.append(i)
        return ans