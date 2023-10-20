# 232. Implement Queue Using Stacks

class MyQueue:

    def __init__(self):
        self.in_stack = list()
        self.out_stack = list()
        self.count = 0 
    

    def push(self, x: int) -> None:
        self.in_stack.append(x)
        self.count += 1
    
    def pop(self) -> int:
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        self.count -= 1
        return self.out_stack.pop()
    
    def peek(self) -> int:
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
        return self.out_stack[-1]
    
    def empty(self) -> bool:
        return self.count == 0


'''
time complexity: push & empty: o(1), pop & peek amortized o(1)
space complexity: o(n)
'''