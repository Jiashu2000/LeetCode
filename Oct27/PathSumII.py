# 113. Path Sum II

class TreeNode:

     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
import collections

class Solution:

    def __init__(self):
        self.res = []
        self.list = []
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: 
            return self.res
        self.backtrack(root, targetSum)
        return self.res


    def backtrack(self, root, targetSum):
        if not root.left and not root.right:
            if targetSum == root.val:
                self.list.append(root.val)
                self.res.append(self.list[:])
                self.list.pop()
            return

        self.list.append(root.val)
        if root.left:
            self.backtrack(root.left, targetSum - root.val)
        if root.right:
            self.backtrack(root.right, targetSum - root.val)
        self.list.pop()
    

    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''



    # iteration
    def pathSum_iteration(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        queue = collections.deque()
        sumqueue = collections.deque()
        
        if not root:
            return res
        
        queue.append([root])
        sumqueue.append(root.val)
        
        while queue:
            curlist = queue.popleft()
            curnode = curlist[-1]
            cursum = sumqueue.popleft()
            if not curnode.left and not curnode.right and cursum == targetSum:
                res.append([node.val for node in curlist])
            if curnode.left:
                ll = curlist[:]
                ll.append(curnode.left)
                queue.append(ll)
                sumqueue.append(cursum + curnode.left.val)
            if curnode.right:                
                rl = curlist[:]
                rl.append(curnode.right)
                queue.append(rl)
                sumqueue.append(cursum + curnode.right.val)
        return res

    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)
    '''

        