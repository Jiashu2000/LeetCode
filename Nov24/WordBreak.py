# 139. Word Break

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for j in range(n+1):
            for i in range(len(wordDict)):
                w = wordDict[i]
                if j >= len(w) and dp[j-len(w)] and s[j-len(w) : j] == w:
                    dp[j] = True
        return dp[n]

