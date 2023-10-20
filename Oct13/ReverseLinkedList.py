# 206. Reverse Linked List

from typing import Optional

class ListNode:

    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:

    # 双指针法
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        cur = head
        pre = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    '''
    time complexity: o(n)
    space complexity: o(1)
    '''


    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        return self.reverseHelper(head, None)

    def reverseHelper(self, cur, pre):
        if cur is None:
            return pre
        tmp = cur.next
        cur.next = pre
        return self.reverseHelper(tmp, cur)
    
    '''
    time complexity: o(n)
    space complexity: o(n) 递归调用了n层栈空间
    '''