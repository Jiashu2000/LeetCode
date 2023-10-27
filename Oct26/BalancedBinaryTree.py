# 110. Balanced Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:

    # recursion method
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        return self.helper(root) != -1
    
    def helper(self, node):
        if not node:
            return 0
        left = self.helper(node.left)
        right = self.helper(node.right)
        if left == -1 or right == -1 or abs(right - left) > 1:
            return -1
        return max(right, left) + 1
    
    '''
    Time complexity: o(n)
        each node in the tree would be accessed once

    Space complexity: o(logn)
    '''