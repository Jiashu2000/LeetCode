# 459. Repeated Substring Pattern

class Solution:

    def repeatedSubstringPattern(self, s: str) -> bool:
        sl = s + s
        sl = sl[1: -1]
        return sl.find(s) != -1
    
    '''
    time complexity: o(n)
    space comlexity: o(n)
    '''

    def kmp_eg(self, s: str) -> bool:
        next = self.getNext(s)
        n = len(s)
        if next[n - 1] != 0 and n % (n - next[n - 1]) == 0:
            return True
        return False


    def getNext(self, s):
        j = 0
        next = [0] * len(s)
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next
    
    '''
    time complexity: o(n)
    space comlexity: o(n)
    '''


        