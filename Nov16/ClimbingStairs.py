# 70. Climbing Stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        first = 1
        second = 2
        for i in range(3, n+1):
            tmp = first + second
            first = second
            second = tmp
        return second