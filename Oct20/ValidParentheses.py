# 20. Valid Parentheses

class Solution:

    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = list()
        for i in range(n):
            cur = s[i]
            if cur in ['(', '{', "["]: 
                stack.append(cur)
            else:
                if cur == ')' and (len(stack) == 0 or stack[-1] != '('):
                    return False
                elif cur == ']' and (len(stack) == 0 or stack[-1] != '['):
                    return False
                elif cur == '}' and (len(stack) == 0 or stack[-1] != '{'):
                    return False
                stack.pop()
        return len(stack) == 0


'''
time complexity: o(n)
space complexity: o(n)
'''