# 337. House Robber III

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        not_used = []
        used = []
        
        stack.append(root)
        while stack:
            cur = stack.pop()
            if cur:
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            else:
                cur = stack.pop()
                right_not_used = right_use = left_not_used = left_use = 0
                if cur.right:
                    right_not_used = not_used.pop()
                    right_use = used.pop()
                if cur.left:
                    left_not_used = not_used.pop()
                    left_use = used.pop()
                used_max = left_not_used + right_not_used + cur.val
                not_used_max = max(left_use + right_use, 
                left_not_used + right_not_used, left_not_used + right_use, left_use + right_not_used)
                not_used.append(not_used_max)
                used.append(used_max) 
        return max(used.pop(), not_used.pop() )   