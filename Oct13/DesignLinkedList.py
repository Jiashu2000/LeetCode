# 707. Design Linked List

class MyLinkedList:

    class ListNode:

        def __init__(self, val = 0, prev = None, next = None):
            self.val = val
            self.prev = prev
            self.next = next   

    def __init__(self):
        self.dummy = MyLinkedList.ListNode()
        self.tail =  MyLinkedList.ListNode()
        self.dummy.next = self.tail
        self.tail.prev = self.dummy
        self.len = 0
        

    def get(self, index: int) -> int:
        ptr = self.dummy
        if index < 0 or index >= self.len:
            return -1
        while index >= 0:
            ptr = ptr.next
            index -= 1
        return ptr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = MyLinkedList.ListNode(val = val)
        newNode.next = self.dummy.next
        self.dummy.next.prev = newNode
        newNode.prev = self.dummy
        self.dummy.next = newNode
        self.len += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = MyLinkedList.ListNode(val = val)
        newNode.prev = self.tail.prev
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        newNode.next = self.tail
        self.len += 1        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.len:
            return
        ptr = self.dummy
        newNode = MyLinkedList.ListNode(val = val)
        while index >= 0:
            ptr = ptr.next
            index -= 1
        prev = ptr.prev
        prev.next = newNode
        newNode.prev = prev
        newNode.next = ptr
        ptr.prev = newNode
        self.len += 1        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.len:
            return
        ptr = self.dummy
        while index >= 0:
            ptr = ptr.next
            index -= 1
        prev = ptr.prev
        prev.next = ptr.next
        ptr.next.prev = prev
        self.len  -= 1  


'''
time complexity: 涉及index的相关操作为o(index), 其余为o(1)
space complexity: o(1)
'''