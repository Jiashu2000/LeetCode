# 104. Maximum Depth of Binary Tree

from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # level order traversal
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return level
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''


    def maxDepth_recursion(self, root: TreeNode) -> int:
        return self.getdepth(root)
    
    def getdepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        left = self.getdepth(root.left)
        right = self.getdepth(root.right)
        return 1 + max(left, right)
    
    '''
    time complexity: o(n)
    space complexity: o(logn)
    '''

'''
二叉树节点的深度：指从根节点到该节点的最长简单路径边的条数或者节点数（取决于深度从0开始还是从1开始）
二叉树节点的高度：指从该节点到叶子节点的最长简单路径边的条数或者节点数（取决于高度从0开始还是从1开始）

使用前序求的就是深度，使用后序求的是高度
根节点的高度就是二叉树的最大深度
'''