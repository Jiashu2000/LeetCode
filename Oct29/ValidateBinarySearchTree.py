# 98. Validate Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

from collections import deque

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False

        return self.helper(root, float("-inf"), float("inf"))
    
    def helper(self, node, min, max):
        if not node:
            return True
        if node.val <= min or node.val >= max:
            return False
        return self.helper(node.left, min, node.val) and self.helper(node.right, node.val, max)
    

    # iteration
    def isValidBST_iteration(self, root: Optional[TreeNode]) -> bool:
        max_queue = deque()
        max_queue.append(float('inf'))
        min_queue = deque()
        min_queue.append(float("-inf"))
        queue = deque()
        queue.append(root)

        while queue:
            cur = queue.popleft()
            right = max_queue.popleft()
            left = min_queue.popleft() 
            if cur.val >= right or cur.val <= left:
                return False
            if cur.right:
                queue.append(cur.right)
                max_queue.append(right)
                min_queue.append(cur.val)
            
            if cur.left:
                queue.append(cur.left)
                max_queue.append(cur.val)
                min_queue.append(left)
        return True
    
    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    
    '''

    def __init__(self):
        self.curmax = float('-inf')

    def isValidBST_eg(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = False

        if root.left:
            left = self.isValidBST_eg(root.left)
        
        if root.left and not left:
            return False

        if root.val <= self.curmax:
            return False

        self.curmax = root.val
        
        return self.isValidBST_eg(root.right)
    


    # iteration
    def isValidBST_iteration_eg(self, root: Optional[TreeNode]) -> bool:
        stack = []
        cur = root
        pre = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if pre and cur.val <= pre.val:
                    return False
                pre = cur
                cur = cur.right
        return True
        
    