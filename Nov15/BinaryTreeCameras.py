# 968. Binary Tree Cameras

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
'''
#1. no require: has camera itself
#2. require parent
#3. no require: child has camera
'''

class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        tot, status = self.helper(root)
        if status == 2:
            return tot + 1 
        return tot
    
    # [the number of cam, status]
    def helper(self, root): 
        if root.left is None and root.right is None:
            return [0, 2]
        
        node_status = 2
        node_sum = 0
        left_sum = 0
        left_status = None
        right_sum = 0
        right_status = None

        if root.left:
            left_sum, left_status = self.helper(root.left)
        if root.right:
            right_sum, right_status = self.helper(root.right)
        
        node_sum = left_sum + right_sum

        # need to have a cam itself
        if left_status == 2 or right_status == 2:
            node_status = 1
            node_sum += 1
        
        # no need to have a cam, covered by one of the child
        elif left_status == 1 or right_status == 1:
            node_status = 3
        
        # children are covered by their children
        # need to require from parent
        elif left_status == 3 and right_status == 3:
            node_status = 2
        
        return [node_sum, node_status]
        


            

        