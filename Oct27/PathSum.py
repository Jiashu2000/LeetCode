# 112. Path Sum

class TreeNode:

     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
import collections

class Solution:

    # recursion
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.backtrack(root, targetSum)
    

    def backtrack(self, root, target):
        if not root.left and not root.right:
            if root.val == target:
                return True
            return False
        
        if root.left:
            if (self.backtrack(root.left, target - root.val)):
                return True
        
        if root.right:
            if (self.backtrack(root.right, target - root.val)):
                return True
        
        return False


    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''

    # iteration
    def hasPathSum_iteration(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        queue = collections.deque()
        pathsum = collections.deque()
        
        queue.append(root)
        pathsum.append(root.val)

        while queue:
            cur = queue.popleft()
            cursum = pathsum.popleft()
            if not cur.left and not cur.right and cursum == targetSum:
                return True
            if cur.left:
                queue.append(cur.left)
                pathsum.append(cursum + cur.left.val)
            if cur.right:
                queue.append(cur.right)
                pathsum.append(cursum + cur.right.val)
        
        return False
    
    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''
