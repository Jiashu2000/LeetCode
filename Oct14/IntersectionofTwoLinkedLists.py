# 160. Intersection of Two Linked Lists

from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1 = 0
        ptr1 = headA
        while ptr1 is not None:
            count1 += 1
            ptr1 = ptr1.next
        count2 = 0
        ptr2 = headB
        while ptr2 is not None:
            count2 += 1
            ptr2 = ptr2.next
        
        ptr1 = headA
        ptr2 = headB
        if count1 >= count2:
            diff = count1 - count2
            while diff > 0:
                ptr1  = ptr1.next
                diff -= 1
        else:
            diff = count2 - count1
            while diff > 0:
                ptr2 = ptr2.next
                diff -= 1
        
        while ptr1 is not None:
            if ptr1 == ptr2:
                return ptr1
            else:
                ptr1 = ptr1.next
                ptr2 = ptr2.next
        
        return None


'''
time complexity: o(m + n)
space compelxity: o(1)
'''