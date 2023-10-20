# 203. Remove Linked List Elements

'''
虚拟头节点的使用
'''
class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


from typing import Optional

class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        prev = dummy
        cur = head

        while cur is not None:
            while cur is not None and cur.val == val:
                cur = cur.next
            prev.next = cur
            prev = cur
            if cur is not None:
                cur = cur.next
        
        return dummy.next


'''
time complexity: o(n)
space complexity: o(1)
'''