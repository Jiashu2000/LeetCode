# 96. Unique Binary Search Trees

class Solution:

    def __init__(self):
        self.dp = dict()
        self.dp[0] = 1
        self.dp[1] = 1
        self.dp[2] = 2

    def numTrees(self, n: int) -> int:
        if n in self.dp:
            return self.dp[n]
        no_tree = 0
        for i in range(n):
            no_tree += self.numTrees(i) * self.numTrees(n-i-1)
        self.dp[n] = no_tree
        return no_tree
            
        
        
        