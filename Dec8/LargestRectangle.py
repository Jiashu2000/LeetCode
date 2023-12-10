# 84.Largest Rectangle in Histogram

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        n = len(heights)
        max_area = 0
        stack = [-1]
        for i in range(n):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
        