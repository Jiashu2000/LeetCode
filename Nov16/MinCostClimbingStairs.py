# 746. Min Cost Climbing Stairs

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n == 1:
            return cost[0]
        first = cost[0]
        second = cost[1]

        for i in range(2, n):
            tmp = min(first, second) + cost[i]
            first = second
            second = tmp
        
        return min(second, first)
        