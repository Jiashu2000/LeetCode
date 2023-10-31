# 450. Delete Node in a BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

'''
5种情况
    1. 没有找到删除节点
    2. 找到删除节点, 左右孩子为空, 返回null为根节点
    3. 删除节点的右节点为空, 左孩子补位, 返回左孩子为根结点
    4. 删除节点的左节点为空, 右孩子补位, 返回右孩子为根结点
    5. 左右孩子都不为空, 将左孩子放在右孩子树最左边节点下, 返回右孩子为根结点
'''



class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # case1: no key found
        if not root:
            return root
        if root.val == key:
            # case2: left,right child are none
            if not root.left and not root.right:
                return None
            # case3: right child is none
            elif not root.right:
                return root.left
            # case4: left child is none
            elif not root.left:
                return root.right
            # case5: both left and right are not none
            else:
                # put the left child under the smallest node of the right child
                cur = root.right
                while cur and cur.left:
                    cur = cur.left
                cur.left = root.left
                return root.right
        elif root.val > key:
                root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    '''
    time: o(n)
    space: o(n)
    '''


    '''
    delete node in a normal binary tree
    swap values
    '''
    def deleteNode_binaryTree(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if root.val == key:
            if not root.right:
                return root.left
            cur = root.right
            while cur.left:
                cur = cur.left
            # 将要删除的节点值与最左节点值交换
            root.val, cur.val=  cur.val, root.val
        root.left = self.deleteNode_binaryTree(root.left, key)
        root.right = self.deleteNode_binaryTree(root.right, key)
        return root
    

            
    def deleteNode_iteration(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        cur = root
        prev = None
        while cur:
            prev = cur
            if cur.val == key:
                break
            elif cur.val > key:
                cur = cur.left
            else:
                cur = cur.right
        if prev == None:
            return self.deleteNodeHelper(self, cur)
        if prev.left and prev.left.val == cur.val:
            prev.left = self.deleteNodeHelper(self, cur)
        elif prev.right and prev.right.val == cur.val:
            prev.right = self.deleteNodeHelper(self, cur)
        return root


    def deleteNodeHelper(self, target):
        '''
        move left child under the smallest node of the right child
        '''
        if not target:
            return target
        if not target.right:
            return target.left
        cur = target.right
        while cur.left:
            cur = cur.left
        cur.left = target.left
        return target.right
              
        
        
        