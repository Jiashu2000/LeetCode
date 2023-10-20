# 28. Find the Index of the First Occurance in a String


# KMP algorithm


class Solution:

    def getNext(self, s: str):
        j = 0 # the end of prefix
        next = [0] * len(s)
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j-1] 
            if s[i] == s[j]:
                j += 1
            next[i] = j
        return next


    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None or haystack is None or len(needle) == 0 or len(haystack) == 0: 
            return -1
        next = self.getNext(needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j -1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - len(needle) + 1
        return -1

'''
time complexity: o(m + n)
space complexity: o(m)
'''
