# 654. Maximum Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List, Optional

class Solution:

    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        self.helper(nums, 0, len(nums)-1)
    


    def helper(self, nums, left, right):
        if right < left:
            return None
        if right == left:
            return nums[left]
        
        maxidx = left
        maxvalue = nums[left]

        for i in range(left, right+1):
            if nums[i] > maxvalue:
                maxvalue = nums[i]
                maxidx = i

        root = TreeNode(nums[maxidx])
        root.left = self.helper(nums, left, maxidx - 1)
        root.right = self.helper(nums, maxidx+1, right)
        return root
    
    '''
    time complexity:
        o(n^2)

    space complexity:
        o(n)    
    '''
                
    def constructMaximumBinaryTree_eg(self, nums: List[int]) -> Optional[TreeNode]:
        stack = []
        for num in nums:
            node = TreeNode(num)
            
            while stack and stack[-1].val < num:
                node.left = stack.pop()
            
            if stack:
                stack[-1].right = node
            
            stack.append(node)
        return stack[0]


    '''
    time complexity: 
        o(n)
    
    space complexity:
        o(n)
    '''