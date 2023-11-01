# 108. Convert Sorted Array to Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional, List
from collections import deque

class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        mid = (len(nums) - 1)//2
        root = TreeNode(nums[mid])
        if len(nums) == 1:
            return root
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
    '''
    time: o(N)
    space: o(N)
    '''

    
    def sortedArrayToBST_iteration(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        root = TreeNode(0)
        node_queue = deque()
        left_queue = deque()
        right_queue = deque()
        node_queue.append(root)
        left_queue.append(0)
        right_queue.append(len(nums) - 1)
        
        while node_queue:
            cur = node_queue.popleft()
            left = left_queue.popleft()
            right =  right_queue.popleft()
            mid = left + (right - left)//2
            cur.val = nums[mid] 

            if left < mid:
                cur.left = TreeNode(0)
                node_queue.append(cur.left)
                left_queue.append(left)
                right_queue.append(mid-1)
            
            if right > mid:
                cur.right = TreeNode(0)
                node_queue.append(cur.right)
                left_queue.append(mid+1)
                right_queue.append(right)
        
        return root

    '''
    time: o(N)
    space: o(N)
    '''