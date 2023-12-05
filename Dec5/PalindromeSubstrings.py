# 647. Palindrome Substrings

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        dp = [[0] * (n) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1): 
            for j in range(i, n):
                if i == j:
                    dp[i][j] = 1
                elif i == j - 1:
                    if s[i] == s[j]:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 0
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 0
        res = 0
        for l in dp:
            res += sum(l)
        return res