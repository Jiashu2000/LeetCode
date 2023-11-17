# 62.unique path


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dp = [[0] * (n+1) for _ in range(2)]
        for i in range(n+1):
            dp[1][i] = 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                dp[0][j] = dp[1][j] + dp[0][j+1]
            dp[1] = dp[0]
    
        
        return dp[0][0]