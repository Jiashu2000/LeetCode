# 452. Minimum Number of Arrows to Burst Balloons

from typing import List 


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key = lambda a : a[0])
        res = 1
        prev_end = points[0][1]
        n = len(points)
        for i in range(1, n):
            cur_start = points[i][0]
            cur_end = points[i][1]
            if cur_start > prev_end:
                res += 1
                prev_end = cur_end
            else:
                prev_end = min(prev_end, cur_end)
        return res

