# 257. Binary Tree Path

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List


class Solution:

    def __init__(self):
        self.list = []
        self.res = []

    # dfs + backtracking
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return self.res
        
        self.backtrack(root)
        return self.res
    
    def backtrack(self, root):
        self.list.append(root.val)
        if not root.left and not root.right:
            self.res.append('->'.join(map(str, self.list)))
            self.list.pop()
            return
        if root.left:
            self.backtrack(root.left)
        if root.right:
            self.backtrack(root.right)
        self.list.pop()
    
    '''
    Time complexity: O(nlogn)
        In the worst case, the tree has (height ** 2) - 1 nodes and there are (n + 1) / 2 leaves. 
        Each root-to-leaf path has length log(n + 1). 
        A string must be created for each root-to-length path.
    Space compexity: O(n)
    
    '''
    
    # dfs + stack
    def binaryTreePaths_iteration(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = []
        path = []
        if not root:
            return res
        
        stack.append(root)
        path.append(str(root.val))
        while stack:
            cur, p = stack.pop(), path.pop()
            if not cur.left and not cur.right:
                res.append(p)
            if cur.left:
                stack.append(cur.left)
                path.append(p + "->" + str(cur.left.val))
            if cur.right:
                stack.append(cur.right)
                path.append(p + "->" + str(cur.right.val))
        return res