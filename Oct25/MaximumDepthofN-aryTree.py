# 559. Maximum Depth of N-ary Tree

import collections

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:


    # recursion
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        curmax = 0
        for child in root.children:
            curmax = max(curmax, self.maxDepth(child))
        return curmax + 1
    
    def maxDepth_iteration(self, root: 'Node') -> int:
        if not root:
            return 0
        queue = collections.deque()
        queue.append(root)
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                cur = queue.popleft()
                for c in cur.children:
                    if c:
                        queue.append(c)
        return level
