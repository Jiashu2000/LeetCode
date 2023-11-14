# 763. Partition Labels

from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        label_dict_last = {}
        res = []

        for i in range(n):
            cur = s[i]
            label_dict_last[cur] = i
        
        left = 0
        right = 0
        i = 0
        while i < n:
            left = i
            right = label_dict_last[s[left]]
            while left < right:
                last_show = label_dict_last[s[left]]
                right = max(right, last_show)
                left += 1
            res.append(right - i + 1)
            i = left + 1
        return res
            
        