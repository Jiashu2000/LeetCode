# 739. Daily Temperatures

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i in range(n):
            cur = temperatures[i]
            if len(stack) == 0 or cur < temperatures[stack[-1]]:
                stack.append(i)
            else:
                while len(stack) > 0 and cur > temperatures[stack[-1]]:
                    idx = stack.pop()
                    ans[idx] = i - idx
                stack.append(i)
        
        return ans
                