# 111. Minimum Depth of Binary Tree


from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # recursion
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return self.minDepth(root.right) + 1
        if not root.right:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
    
    '''
    time complexity: o(n)
    space complexity: o(logn)
    '''


    # iteration
    def minDepth_iterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = collections.deque()
        stack.append(root)
        level = 1
        while stack:
            size = len(stack)
            for i in range(size):
                cur = stack.popleft()
                if not cur.left and not cur.right:
                    return level
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            level += 1 
        return -1

    '''
    time complexity: o(n)
    space complexity: o(n)
    '''