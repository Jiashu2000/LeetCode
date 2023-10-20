# 904. Fruit into Baskets

from typing import List

class Solution:
    
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        max_pick = 0
        left = 0
        right = 0 
        pick_count = {}

        while right < n:
            type = fruits[right]
            pick_count[type] = pick_count.get(type, 0) + 1

            if len(pick_count.keys()) <= 2:
                max_pick = max(max_pick, right - left + 1)
            
            while len(pick_count.keys()) > 2:
                remove_type = fruits[left]
                pick_count[remove_type] = pick_count[remove_type] - 1
                if pick_count[remove_type] == 0:
                    pick_count.pop(remove_type)
                left += 1
            
            right += 1
        
        return max_pick


'''
time complexity: o(n)
space complexity: o(1)
'''