# 225. Implement Stack Using Queue

from collections import deque

class MyStack:


    def __init__(self):
        self.queue = deque()
        self.count = 0

    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(self.count):
            self.queue.append(self.queue.popleft())
        self.count += 1
    
    def pop(self) -> int:
        self.count -= 1
        return self.queue.popleft()
    
    def top(self) -> int:
        return self.queue[0]
    
    def empty(self) -> bool:
        return self.count == 0
    

'''
time complexity: push: o(n); pop, top, empty: o(1)
space complexity: o(n)
'''