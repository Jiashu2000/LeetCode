# 617. Merge Two Binary Trees

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    # recursion
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root = TreeNode(root1.val + root2.val)
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root


    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''


    # iteration
    def mergeTrees_iteration(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1
        
        queue = deque()
        queue.append(root1)
        queue.append(root2)
        
        while queue:
            cur1 = queue.popleft()
            cur2 = queue.popleft()
            cur1.val += cur2.val

            if cur1.left and cur2.left:
                queue.append(cur1.left)
                queue.append(cur2.left)

            
            if cur1.right and cur2.right:
                queue.append(cur1.right)
                queue.append(cur2.right)
            
            if (not cur1.left) and cur2.left:
                cur1.left = cur2.left

            if (not cur1.right) and cur2.right:
                cur1.right = cur2.right
            
        
        return root1
    
    '''
    time complexity:
        o(n)

    space complexity:
        o(n)
    
    '''

        