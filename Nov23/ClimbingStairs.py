# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(2, n):
            tmp = first + second
            first = second
            second = tmp 
        return second