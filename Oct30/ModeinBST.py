# 501. Find Mode in Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List

class Solution:

    def __init__(self) -> None:
        self.count = {}
        self.maxcount = 0
        self.res = []

    # recursion
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.res
        self.traverse(root)
        return self.res
    
    def traverse(self, node):
        if not node:
            return
        if node.val not in self.count:
            self.count[node.val] = 0
        
        self.count[node.val] += 1
        if self.count[node.val] == self.maxcount:
            self.res.append(node.val)
        elif self.count[node.val] > self.maxcount:
            self.maxcount = self.count[node.val]
            self.res = [node.val]
        
        if node.left:
            self.traverse(node.left)
        
        if node.right:
            self.traverse(node.right)
    

    '''
    time complexity:
        o(n)
    
    space complexity:
        o(n)    
    '''

    

    def findMode_recursion2(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        if not root:
            return stack
        self.traverse(root, stack)
        maxlen = 1
        res = []
        i = 0
        while i < len(stack):
            j = i
            while j < len(stack) and stack[j] == stack[i]:
                j += 1
            if j - i > maxlen:
                maxlen = j - i
                res = [stack[i]]
            elif j - i == maxlen:
                res.append(stack[i])
            i = j
        return res
    

    def traverse(self, root, stack):
        if not root:
            return
        if root.left:
            self.traverse(root.left)
        stack.append(root.val)
        if root.right:
            self.traverse(root.right)

    # iteration
    def findMode_iteration(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        prev = None
        prevcount = 0
        maxcount = 0
        if not root:
            return res
        stack = []
        cur = root
        while stack or cur:

            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()

                '''
                specify is None or not:
                do not use if not!! special case of 0!1
                
                '''
                if prev is None or prev != cur.val:
                    prevcount = 1
                    prev = cur.val
                else:
                    prevcount += 1

                if prevcount > maxcount:
                    maxcount = prevcount
                    res = [prev]
                elif prevcount == maxcount:
                    res.append(prev)
                
                cur = cur.right

        return res
                
                    
                        
