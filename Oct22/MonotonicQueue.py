# 单调队列

from collections import deque

class MyQueue:

    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft() # time complexity is o(n) is we use list
    
    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)
    
    def front(self):
        return self.queue[0]

