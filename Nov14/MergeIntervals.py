# 56. Merge Intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)

        if not intervals:
            return res
        intervals.sort(key = lambda a: a[0])

        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for i in range(1, n):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]

            if cur_start <= prev_end:
                prev_end = max(prev_end, cur_end)
            else:
                res.append([prev_start, prev_end])
                prev_start = cur_start
                prev_end = cur_end
    
        res.append([prev_start, prev_end])

        return res