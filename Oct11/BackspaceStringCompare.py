# 844. Backspace String Compare

class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        sptr = m - 1
        tptr = n - 1
        sback = 0
        tback = 0 

        while sptr >= 0 and tptr >= 0:
            
            while sptr >= 0 and s[sptr] == '#':
                sback += 1
                sptr -= 1

                while sptr >= 0 and sback > 0:
                    if s[sptr] == '#':
                        sback += 1
                    else:
                        sback -= 1
                    sptr -= 1
            
            while tptr >= 0 and t[tptr] == '#':
                tback += 1
                tptr -= 1
        
                while tptr >= 0 and tback > 0:
                    if t[tptr] == '#':
                        tback += 1
                    else:
                        tback -= 1
                    tptr -= 1

            if sptr == -1 and tptr == -1:
                return True  

            if s[sptr] != t[tptr]:
                return False

            sptr -= 1
            tptr -= 1

        while sptr >= 0 and s[sptr] == '#':
            sback += 1
            sptr -= 1

            while sptr >= 0 and sback > 0:
                if s[sptr] == '#':
                    sback += 1
                else:
                    sback -= 1
                sptr -= 1
            
        while tptr >= 0 and t[tptr] == '#':
            tback += 1
            tptr -= 1
    
            while tptr >= 0 and tback > 0:
                if t[tptr] == '#':
                    tback += 1
                else:
                    tback -= 1
                tptr -= 1
        
        return sptr == -1 and tptr == -1
    
    '''
    time complexity: o(n)
    space complexity: o(1)
    '''

    def twopointer(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        sback, tback = 0, 0 

        while True:
            while i >= 0 and (sback > 0 or s[i] == '#'):
                sback += 1 if s[i] == '#' else -1
                i -= 1
            
            while j >= 0 and (tback > 0 or t[j] == '#'):
                tback += 1 if t[j] == '#' else -1
                j -= 1
            
            if (i < 0) or (j < 0) or (s[i] != t[j]):
                return i == j == -1
            i, j = i - 1, j - 1

