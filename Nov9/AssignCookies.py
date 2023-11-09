# 455. Assign Cookies

from typing import List

class Solution:

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        gptr = len(g) - 1
        sptr = len(s) - 1
        res = 0

        while sptr >= 0 and gptr >= 0:
            if s[sptr] >= g[gptr]:
                res += 1
                sptr -= 1
                gptr -= 1
            else:
                gptr -= 1
        return res

'''
time: o(n)
space: o(1)
'''