# 669. Trim a Binary Search Tree

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursion
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        # root is none
        if not root:
            return None
        
        if root.val < low:
            return self.trimBST(root.right, low, high)

        elif root.val > high:
            return self.trimBST(root.left, low, high)
        
        else:
            root.left = self.trimBST(root.left, low, high)
            root.right = self.trimBST(root.right, low, high)
        return root
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''

    def trimBST_iteration(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return None
        # deal with condition when root is not in the range
        while root and (root.val < low or root.val > high):
            if root.val < low:
                root = root.right
            elif root.val > high:
                root = root.left
        
        cur = root
        # root is in the range
        # deal with left node
        while cur:
            while cur.left and cur.left.val < low:
                cur.left = cur.left.right
            cur = cur.left
        
        cur = root
        # root is in the range
        # deal with right node
        while cur:
            while cur.right and cur.right.val > high:
                cur.right = cur.right.left
            cur = cur.right
        
        return root

    '''
    time complexity: o(n)
    space complexity: o(1)
    '''    
        