# 538. Convert BST to Greater Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        tot = 0
        if not root:
            return root
        stack = []
        stack.append(root)

        while stack:
            cur = stack.pop()
            if cur:
                if cur.left:
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
                if cur.right:
                    stack.append(cur.right)
            else:
                cur = stack.pop() 
                tot = cur.val + tot
                cur.val = tot
        return root
    
    '''
    time: o(n)
    space: o(n)
    '''