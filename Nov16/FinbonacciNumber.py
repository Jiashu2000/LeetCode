# 509. Finbonacci Number


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        
        first = 0
        second = 1
        for i in range(2, n+1):
            tmp = first + second
            first = second
            second = tmp
        return second
        