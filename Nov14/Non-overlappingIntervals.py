# 435. Non-overlapping Intervals 

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x : x[0])
        res = 0
        if not intervals:
            return res
        
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]

        for i in range(1, n):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if cur_start < prev_end:
                res += 1
                prev_end = min(cur_end, prev_end)
            else:
                prev_start = cur_start
                prev_end = cur_end
        
        return res
        