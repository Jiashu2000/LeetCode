# 343. Integer Break

class Solution:

    def __init__(self):
        self.tbl = dict()
        self.tbl[1] = 1
        self.tbl[2] = 1

    def integerBreak(self, n: int) -> int:
        if n in self.tbl:
            return self.tbl[n]
        max_prod = 0
        for i in range(1, n//2+1):
            a = self.integerBreak(i)
            b = self.integerBreak(n-i)
            prod = max(a * b, i * (n-i), i * b, a* (n-i))
            max_prod = max(max_prod, prod)
        self.tbl[n] = max_prod
        return self.tbl[n]

'''
time complexity: O(n^2)
space complexity: O(n)
'''