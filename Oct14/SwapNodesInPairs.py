# 24. Swap Nodes in Pairs

from typing import Optional

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        self.helper(head, dummy)
        return dummy.next
    

    def helper(self, head, pre):
        if head is None or head.next is None:
            pre.next = head
            return
        rest = head.next.next
        pre.next = head.next
        head.next.next = head
        self.helper(rest, pre.next.next)
    

    def swapPair2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        pre = dummy
        ptr = head

        while ptr is not None and ptr.next is not None:
            rest = ptr.next.next

            pre.next = ptr.next
            ptr.next.next = ptr
            ptr.next = rest
            ptr = rest
            pre = pre.next.next
        return dummy.next
    
    '''
    time complexity: o(n)
    space complexity: o(1)
    '''
