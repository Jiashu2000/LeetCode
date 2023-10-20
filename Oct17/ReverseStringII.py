# 541. Reverse String II

class Solution:

    def reverseStr(self, s: str, k: int) -> str:
        
        n = len(s)
        s = list(s)
        ptr = 0
        while ptr <= n - 2*k:
            left = ptr
            right = ptr + k - 1
            while right < n and left < right:
                s[right], s[left] = s[left], s[right]
                left += 1
                right -= 1
            ptr += 2 * k

        left = ptr
        right = ptr
        if n - ptr < k:
            right = n - 1
        else:
            right = left + k -1
        
        while right < n and left < right:
            s[right], s[left] = s[left], s[right]
            left += 1
            right -= 1

        return ''.join(x for x in s)
    

    def reverseString_eg1(self, s: str, k: int) -> str:

        def reverse_string(text):
            left, right = 0, len(text) - 1
            while left < right:
                text[left], text[right] = text[right], text[left]
                left += 1
                right -= 1
            return text
        
        res = list(s)


        for cur in range(0, len(s), 2*k):
            res[cur: cur+k] = reverse_string(res[cur: cur+k])
    
        return ''.join(res)
    


    def reverseString_eg2(self, s: str, k: int) -> str:
        
        p = 0
        while p < len(s):
            p2 = p + k
            s = s[:p] + s[p : p2][::-1] + s[p2:]
            p = p + 2 * k
        return s
    

    '''
    time complexity: o(n)
    space complexity: o(1)
    '''

        
