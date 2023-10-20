# 76. Minimum Window Substring

class Solution:

    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""
        
        char_dict = {}
        for i in t:
            char_dict[i] = char_dict.get(i, 0) + 1
        
        window_dict = {}
        
        # record the rightmost index for every character
        idx_dict = {}
        left = 0
        right = 0
        min_len = m + 1
        min_str = ""
        
        while right < m:
            char = s[right]
            window_dict[char] = window_dict.get(char, 0) + 1
            idx_dict[char] = right

            # update the left window
            while left <= right:
                left_char = s[left]
                if (left_char in char_dict.keys() and idx_dict[left_char] == left) or (left_char in char_dict.keys() and window_dict[left_char] <= char_dict[left_char]):
                    break
                window_dict[left_char] = window_dict[left_char] - 1
                left += 1
        
            # all chars in t are included in window
            if self.include(char_dict, window_dict):
                if right - left + 1 < min_len:
                    min_str = s[left : right + 1]
                    min_len = right - left + 1
            right += 1
            
        
        return min_str
    

    def include(self, char_dict, window_dict):
        for k in char_dict.keys():
            if k not in window_dict.keys() or window_dict[k] < char_dict[k]:
                return False
        return True
                
'''
time complexity: o(m + n)
space complexity: o(m + n)
'''
                
            

        
        
