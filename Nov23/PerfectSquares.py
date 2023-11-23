# 279. Perfect Squares

class Solution:
    def numSquares(self, n: int) -> int:
        perfect_squares = []
        i = 1
        while i**2 <= n:
            perfect_squares.append(i**2)
            i += 1
        dp = [n] * (n + 1)
        dp[0] = 0
        for k in perfect_squares:
            for j in range(1, n+1):
                if j - k >= 0: 
                    dp[j] = min(dp[j], dp[j-k] + 1)
        return dp[n]
                