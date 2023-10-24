# 二叉树的层序遍历

'''
队列先进先出，符合一层一层遍历的逻辑。栈先进后出，符合模拟深度优先也就是递归的逻辑
层序遍历就是广度优先遍历

'''

from typing import Optional, List
import collections

class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left
    
class Solution: 
    
    def levelOrder_iteration(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result
    


    def levelOrder_recursion(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        self.helper(root, 0, levels)
        return levels
    
    def helper(self, node, level, levels):
        if not node:
            return
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)
        self.helper(node.left, level + 1, levels)
        self.helper(node.right, level+1, levels)
    

# 107. Binary Tree Level Order Traversal II

    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            while size > 0:
                pop = queue.popleft()
                level.append(pop.val)
                if pop.left:
                    queue.append(pop.left)
                if pop.right:
                    queue.append(pop.right)
                size -= 1
            levels.append(level)
        return levels[::-1]

    '''
    time complexity: o(n)
    space complexity: o(n)
    where n is the number of treenodes
    '''


# 199. Binary Tree Right Side View

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if i == size - 1:
                    res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        return res
    '''
    time complexity: o(n)
    space complexity: o(n)
    where n is the number of treenodes
    '''

# 637. Average of Levels in Binary Tree
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            tot = 0
            for _ in range(size):
                cur = queue.popleft()
                tot += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(tot/size)
        return res
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    where n is the number of treenodes
    '''

# 429. N-ary Tree Level Order Traversal

    class NNode:
        
        def __init__(self, val = None, children = None):
            self.val = val
            self.children = children
            
    def levelOrder(self, root: "NNode") -> List[List[int]]:
        if not root: 
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            level = []
            for _ in range(size):
                cur = queue.popleft()
                level.append(cur.val)
                for c in cur.children:
                    queue.append(c)
            res.append(level)
        return res
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''

# 515. Find Largest Value in Each Tree Row

    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            curMax = float('-inf')
            for i in range(size):
                cur = queue.popleft()
                curMax = max(curMax, cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(curMax)
        return res
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''

# 116. Populating Next Right Pointers in Each Node

    class Node:

        def __init__(self, val: int = 0, left: "Solution.Node" = None, 
                     right: 'Solution.Node' = None, next: 'Solution.Node' = None):
            self.val = val
            self.left = left 
            self.right = right
            self.next = next
        
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            prev = None
            cur = None
            for i in range(size):
                cur = queue.popleft()
                if prev:
                    prev.next = cur
                prev = cur
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            cur.next = None
        return root
            
        '''
        time complexity: o(n)
        space complexity: o(n)
        '''


# 117. Populating Next Right Pointers in Each Node II
# the same as the last question

# 104. Maximum Depth of Binary Tree

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


# 111. Minimum Depth of Binary Tree

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if root.left is None and root.right is None:
            return 1
        left = right = float('inf')
        if root.left:
            left = self.minDepth(root.left)
        if root.right:
            right = self.minDepth(root.right)
        return min(left, right) + 1