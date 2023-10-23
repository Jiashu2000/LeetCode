# 二叉树的递归遍历

from typing import List

'''
递归的三要素
    1. 确定递归函数的参数和返回值: 哪些参数是递归的过程中需要处理的，那么就在递归函数里加上这个参数。
        同时明确每次递归的返回值是什么进而确定确定函数的返回类型。
    2. 确定终止条件: 如果递归没有终止，操作系统的内存栈必然会溢出。
    3. 确定单层递归的逻辑: 确定每一层递归要处理的信息。
'''

class TreeNode:

    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Traversal:

    # 递归遍历

    def preorder_recursion(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left = self.preorder(root.left)
        right = self.preorder(root.right)
        
        return [root.val] + left + right
    
    def inorder_recursion(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left = self.inorder(root.left)
        right = self.inorder(root.right)
        
        return left + [root.val] + right
    
    def postorder_recursion(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        left = self.postorder(root.left)
        right = self.postorder(root.right)

        return left + right + [root.val]
    
    # 迭代遍历

    def preorder_iteration(self, root: TreeNode) -> List[int]:
        # 中左右
        if not root:
            return []
        
        res = []
        stack = []
        stack.append(root)
        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.right is not None:
                stack.append(pop.right)
            if pop.left is not None:
                stack.append(pop.left)
        return res
    

    '''
    在迭代过程中，我们有两个操作
    1. 处理: 将元素放进result数组
    2. 访问: 遍历节点

    前序遍历: 要访问的元素和要处理的元素顺序是一致的，都是中间节点
    中序遍历: 要访问的元素和要处理的元素顺序不一致，要用指针的遍历访问节点，栈处理节点元素
    '''
    
    def inorder_iteration(self, root: TreeNode) -> List[int]:
        # 左中右
        if not root:
            return []
        
        res = []
        stack = []
        cur = root

        while cur is not None or len(stack) > 0:
            if cur is not None:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
    
    def postorder_iteration(self, root: TreeNode) -> List[int]:
        # 左右中
        if not root:
            return []
        
        stack = []
        res = []
        stack.append(root)

        while stack:
            pop = stack.pop()
            res.append(pop.val)
            if pop.left:
                stack.append(pop.left)
            if pop.right:
                stack.append(pop.right)
        
        return res[::-1]
            
    # 迭代法统一写法
    '''
    就将访问的节点放入栈中，把要处理的节点也放入栈中但是要做标记。
    如何标记呢，就是要处理的节点放入栈之后，紧接着放入一个空指针作为标记。 这种方法也可以叫做标记法。  
    '''

    def preorder_iteration2(self, root: TreeNode):
        # 中左右
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
                stack.append(node)
                stack.append(None)
            else:
                node = stack.pop()
                res.append(node.val)
        return res


    def inorder_iteration2(self, root: TreeNode):
        # 左中右
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            if node:
                if node.right:
                    stack.append(node.right)
                stack.append(node)
                stack.append(None)
                if node.left:
                    stack.append(node.left)
            else:
                cur = stack.pop()
                res.append(cur.val)
        return res

    def postorder_iteration2(self, root: TreeNode):
        # 左右中
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)

        while stack:
            node = stack.pop()
            if node:
                stack.append(node)
                stack.append(None)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                node = stack.pop()
                res.append(node.val)
        return res