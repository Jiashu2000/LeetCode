# 222. Count Complete Tree Nodes

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
完全二叉树的特性
'''

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = 0
        left = root
        while left:
            lh += 1
            left = left.left
        
        rh = 0
        right = root
        while right:
            rh += 1
            right = right.right
        
        if lh == rh:
            return pow(2, lh) - 1
        
        return self.countNodes(root.right) + self.countNodes(root.left) + 1
    
    '''
    time complexity:
        recursion(logn) * find height(logn) = (logn)^2
    space complexity:
        o(logn)
    '''

    def countNodes_eg(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left, right = root.left, root.right
        
        count = 0
        while left and right:
            count += 1
            left ,right = left.left, right.right
        
        if not left and not right:
            # this is faster than pow!
            return (2<<count) - 1
        return self.countNodes_eg(root.left) + self.countNodes_eg(root.right) + 1