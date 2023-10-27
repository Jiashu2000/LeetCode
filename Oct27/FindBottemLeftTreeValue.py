# 513. Find Bottem Left Tree Value

class TreeNode:

     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import collections

class Solution:

    # iteration
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque()
        queue.append(root)
        list = []
        while queue:
            size = len(queue)
            list = []
            for i in range(size):
                cur = queue.popleft()
                list.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return list[0]
    
    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''

    # recursion
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)[1]
    
    def helper(self, root):
        if not root.left and not root.right:
            return [0, root.val]
        left = None
        right = None
        if root.left:
            left = self.helper(root.left)
        if root.right:
            right = self.helper(root.right)
        
        if (left and right and left[0] < right[0]) or not left:
            return [right[0] + 1, right[1]]
        return [left[0]+1, left[1]]
    
    '''
    time complextiy:
        o(n)
    
    space complexity:
        o(n)
    '''
                