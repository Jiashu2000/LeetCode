# 142. Linked List Cycle II


from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
    

class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

'''
time complexity: o(n)
space complexity: o(1)
'''