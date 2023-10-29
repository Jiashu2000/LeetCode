# 700. Search in a Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    # recursion
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == val:
            return root
        
        if root.val > val:
            return self.searchBST(root.left, val)
        
        return self.searchBST(root.right, val)
    
    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    
    '''

    # iteration
    # 二叉搜索树的有序性
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val == val: 
                return root
            if root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    '''
    time complexity:
        o(n)
    
    space complexity:
        o(1)
    
    '''