# 236. Lowest Common Ancestor of a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
            
        if left and right:
            return root
        
        elif left or right:
            if root.val == p.val or root.val == q.val:
                return root        
            
            if left:
                return left
            return right

        if root.val == p.val or root.val == q.val:
                        return root   
            
        return None

    '''
    time:
        o(n)
    
    space:
        o(n)
    
    '''