# 242. Valid Anagram

class Solution:

    def isAnagram(self, s: str, t: str) -> bool:
        if s is None and t is None:
            return True
        count = [0] * 26
        for i in s:
            idx = ord(i) - ord('a')
            count[idx] += 1
        for j in t:
            idx = ord(j) - ord('a')
            count[idx] -= 1
        for i in count:
            if i != 0:
                return False
        return True
    

'''
time complexity=: o(n)
space complexity: o(1)
'''