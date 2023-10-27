# 106. Construct Binary Tree from Inorder and Postorder Traversal

class TreeNode:

     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not postorder:
            return None
        return self.helper(inorder, 0, len(inorder) - 1, postorder, 0, len(postorder) - 1)
        
    
    def helper(self, inorder, istart, iend, postorder, pstart, pend):
        if iend < istart or pend < pstart:
            return None
        if iend == istart:
            return TreeNode(inorder[istart])

        root = TreeNode(postorder[pend])
        # could use an index map to save the time
        idx = inorder.index(root.val)
        leftlen = idx - istart
        rightlen = iend - idx
        
        root.left = self.helper(inorder, istart, idx - 1, postorder, pstart, pend - rightlen - 1)
        root.right = self.helper(inorder, idx+1, iend, postorder, pend-rightlen, pend - 1)   
        return root 

    '''
    time complexity:
        o(n^2)
    
    space complexity:
        o(n)
    
    ''' 
        
        