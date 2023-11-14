# 860. Lemonade Change

from typing import List

class Solution:
    
    def lemonadeChange(self, bills: List[int]) -> bool:
        changes = [0] * 3
        n = len(bills)
        for i in range(n):
            pay = bills[i]
            if pay == 5:
                changes[0] += 1
                continue
            elif pay == 10:
                changes[1] += 1
                if changes[0] == 0:
                    return False
                changes[0] -= 1
            else:
                changes[2] += 1
                if changes[1] > 0:
                    changes[1] -= 1
                    if changes[0] == 0:
                        return False
                    changes[0] -= 1
                else:
                    if changes[0] < 3:
                        return False
                    changes[0] -= 3
        return True
 