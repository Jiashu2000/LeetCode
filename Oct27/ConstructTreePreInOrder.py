# 105. Construct Binary Tree from Preorder and Inorder Traversal

class TreeNode:

     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder or not preorder:
            return None
        return self.helper(inorder, 0, len(inorder)-1, preorder, 0, len(preorder)-1)

    def helper(self, inorder, istart, iend, preorder, pstart, pend):
        if iend < istart or pend < pstart:
            return None
        if iend == istart:
            return TreeNode(inorder[iend])
        
        root = TreeNode(preorder[pstart])
        idx = inorder.index(root.val)
        leftlen = idx - istart
        rightlen = iend - idx

        root.left = self.helper(inorder, istart, idx - 1, preorder, pstart + 1, pstart + leftlen)
        root.right = self.helper(inorder, idx+1, iend, preorder, pstart+leftlen +1, pend)
        return root
    
    '''
    time complexity:
        o(n^2)
    
    space complexity:
        o(n)
    
    '''