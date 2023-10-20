# 19. Remove Nth Node From End of List

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    
from typing import Optional

class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        fast = dummy
        slow = dummy

        while fast is not None and n >= 0:
            fast = fast.next
            n -= 1
        
        while fast is not None:
            fast = fast.next
            slow = slow.next
    
        if slow is not None and slow.next is not None:
            slow.next = slow.next.next
    
        return dummy.next
    
    '''
    time complexity: o(n)
    space complexity: o(1)
    '''