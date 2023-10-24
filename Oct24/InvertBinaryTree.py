# 226. Invert Binary Tree

class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        if root.left is None and root.right is None:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.left = right
        root.right = left
        return root

    def invertTree_iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = []
        stack.append(root)
        while stack:
            cur = stack.pop()
            cur.left, cur.right = cur.right, cur.left 
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return root