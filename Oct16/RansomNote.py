# 383. Ransom Note

class Solution:


    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        count = [0] * 26
        for s in magazine:
            idx = ord(s) - ord('a')
            count[idx] += 1
        
        for s in ransomNote:
            idx = ord(s) - ord('a')
            count[idx] -= 1
            if count[idx] < 0:
                return False
        
        return True


'''
time complexity: o(n)
space complexity: o(1)
'''