# 150. Evaluate Reverse Polish Notation

from typing import List

class Solution:

    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        n = len(tokens)
        for i in range(n):
            cur = tokens[i]
            if cur.lstrip("-").isdigit():
                num_stack.append(int(cur))
            else:
                a = num_stack.pop()
                b = num_stack.pop()
                if cur == '+':
                    num_stack.append(a+b)
                elif cur == '-':
                    num_stack.append(b-a)
                elif cur == "*":
                    num_stack.append(a*b)
                else:
                    t = b // a
                    if b%a != 0 and t < 0:
                        t += 1
                    num_stack.append(t)
        return num_stack[0]
    
'''
time complexity: o(n)
space complexity: o(n)


波特兰表达式相当于是二叉树的后序遍历
后缀表达式对于计算机是非常友好的

'''

