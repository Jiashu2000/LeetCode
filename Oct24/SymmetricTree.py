# 101. Symmetric Tree 

import collections

class TreeNode:
    
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

from typing import Optional

class Solution:

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.helper(root.left, root.right)
    
    def helper(self, leftsub, rightsub):
        if leftsub is None and rightsub is None:
            return True
        if leftsub is None or rightsub is None:
            return False
        if leftsub.val != rightsub.val: 
            return False
        return self.helper(leftsub.left, rightsub.right) and self.helper(leftsub.right, rightsub.left)
    
    '''
    time complexity: o(n)
    space complexity: o(n)
    '''
    # iteration, queue
    def isSymmetric_iteration_queue(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        queue = collections.deque()
        queue.append(root.left)
        queue.append(root.right)
        while queue:
            left = queue.popleft()
            right = queue.popleft()
            if left is None and right is None:
                continue
            if left is None or right is None or left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True


    # iteration, stack
    def isSymmetric_iteration_stack(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        stack = []
        stack.append(root.left)
        stack.append(root.right)
        while stack:
            right = stack.pop()
            left = stack.pop()
            if right is None and left is None:
                continue
            if right is None or left is None or left.val != right.val:
                return False
            stack.append(left.left)
            stack.append(right.right)
            stack.append(left.right)
            stack.append(right.left)
        return True

    # iteration, level-order traversal
    def isSymmetric_iteration_stack(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return root
        levels = []
        queue = collections.deque([root])
        while queue:
            size = len(queue)
            level = []
            for i in range(size):
                cur = queue.popleft()
                level.append(cur)
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
            left, right = 0, size - 1
            while left < right:
                leftnode, rightnode = level[left], level[right]
                if not leftnode and not rightnode:
                    left += 1
                    right -= 1
                    continue
                elif not leftnode or not rightnode or leftnode.val != rightnode.val:
                    return False
                left += 1 
                right -= 1
        return True