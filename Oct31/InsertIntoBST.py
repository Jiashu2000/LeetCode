# 701. Insert into a Binary Search Tree

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:

    #recursion
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        if root.val > val:
            if root.left:
                self.insertIntoBST(root.left, val)
            else:
                root.left = TreeNode(val)
        elif root.val < val:
            if root.right:
                self.insertIntoBST(root.right, val)
            else:
                root.right = TreeNode(val)
        return root
    
    '''
    time: o(n)
    space: o(n)
    '''

    #iteration
    def insertIntoBST_iteration(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        while cur:
            if cur.val > val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = TreeNode(val)
                    return root
            elif cur.val < val:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = TreeNode(val)
                    return root

    '''
    time: o(n)
    space: o(1)
    '''
        
        