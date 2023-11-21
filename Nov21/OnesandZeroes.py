# 474. Ones and Zeroes

from typing import List


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            s_m = 0
            s_n = 0
            for k in s:
                s_m += 1 if k == '0' else 0
                s_n += 1 if k == '1' else 0

            for i in range(m, s_m - 1, -1):
                for j in range(n, s_n -1, -1):
                    if i - s_m == 0 and j - s_n == 0:
                        dp[i][j] = max(dp[i][j], 1)
                    elif dp[i - s_m][j - s_n] > 0:
                        dp[i][j] = max(dp[i][j], dp[i - s_m][j - s_n] + 1)

        ans = 0
        for arr in dp:
            ans = max(max(arr), ans)
        return ans                   
                