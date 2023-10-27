# 404. Sum of Left Leaves

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
import collections

class Solution:

    # recursion
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            res += root.left.val
        res += self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res  
    
    '''
    Time complexity: o(n)
    Space complexity: o(h)
    '''
    
    # iteration
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = collections.deque() 
        queue.append(root)
        while queue:
            cur = queue.popleft()
            if cur.left and not cur.left.left and not cur.left.right:
                res += cur.left.val
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        return res 
    
    '''
    Time complexity: o(n)
    Space complexity: o(h)
    '''