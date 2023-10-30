# 530. Minimum Absolute Difference in BST

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:


    # recursion
    def __init__(self):
        self.min_diff = float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # special case when root is none
        if not root:
            return 0
        self.helper(root, float('-inf'), float('inf'))
        return self.min_diff
    
    def helper(self, node, max, min):
        self.min_diff = min(self.min_diff, abs(max - node.val))
        self.min_diff = min(self.min_diff, abs(min - node.val))
        if node.left:
            self.helper(node.left, node.val, min)
        if node.right:
            self.helper(node.right, max, node.val)
    
    '''
    time complexity:
        o(n): each node compared three times at most
    
    space complexity: 
        o(n): recursion could called o(n) times at most
    '''
        

    # iteration
    def getMinimumDifference_iteration(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = []
        cur = root
        prev = None
        min_diff = float('inf')

        while stack or cur:
            if cur:
                print(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if prev:
                    min_diff = min(min_diff, abs(cur.val - prev.val))
                prev = cur
                cur = cur.right
        return min_diff
    
    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''

    def getMinimumDifference_iteration2(self, root: Optional[TreeNode]) -> int:
        stack = []
        stack.append(root)
        prev = None
        min_diff = float('inf')

        while stack:
            cur = stack.pop()
            if cur:
                # 遍历
                if cur.right: 
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left:
                    stack.append(cur.left)
            else:
                # 处理
                cur = stack.pop()
                if prev:
                    min_diff = min(min_diff, abs(prev.val - cur.val))
                prev = cur
        return min_diff
                