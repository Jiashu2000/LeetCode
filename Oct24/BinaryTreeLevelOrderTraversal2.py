# 107. Binary Tree Level Order Traversal II

class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
    

from typing import Optional, List
import collections

class Solution:

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            while size > 0:
                pop = queue.popleft()
                level.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                size -= 1
            levels.append(level)
        return levels[::-1]
        