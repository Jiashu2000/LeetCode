# 93. Restoring IP Addresses


from typing import List


class Solution:

    def __init__(self) -> None:
        self.res = []
        self.ip = []

    def restoreIpAddresses(self, s: str) -> List[str]:
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s, idx):
        if idx >= len(s) or len(self.ip) >= 4:
            if idx >= len(s) and len(self.ip) == 4:
                s = ""
                for i in self.ip:
                    s = s + str(i) + '.'
                self.res.append(s[:-1])
            return
        
        for i in range(idx+1, min(len(s)+1, idx+4)):
            if i > idx + 1 and s[idx] == '0':
                break
            sub = int(s[idx : i])
            if sub >= 0 and sub <= 255:
                self.ip.append(sub)
                self.backtrack(s, i)
                self.ip.pop()      
        
'''
time: 
    O(3^4)
    ip address has at most 4 numbers. each number has at most three ways of division.
    搜索树的最大深度为4, 每个节点最多有三个子节点

space:
    O(n)
'''