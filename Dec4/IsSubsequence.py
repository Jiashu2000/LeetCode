# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        n = len(s)
        m = len(t)
        p = 0

        for i in range(n): 
            c = s[i]
            while p < m and t[p] != c:
                p += 1
            if p >= m:
                return False
            p += 1
        
        return True


