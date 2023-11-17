# 63. Unique Paths 

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[0] * (n+1) for _ in range(2)]

        i = n - 1
        while i >= 0 and obstacleGrid[m-1][i] != 1:
            dp[1][i] = 1
            i -= 1
        
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[0][j] = 0
                else:
                    dp[0][j] = dp[1][j] + dp[0][j+1]
            dp[1] = dp[0]
        
        
        return dp[1][0]