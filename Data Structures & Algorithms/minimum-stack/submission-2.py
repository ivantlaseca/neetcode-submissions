"""
Use a list

pop, top are built-in funcs

push:
Use separate minStack, where we push the smallest element on each push

getMin:
return the top of minStack

"""

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
    
    def push(self, val: int):
        self.stack.append(val)
        if self.minStack:
            val = min(self.minStack[-1], val)
        self.minStack.append(val)
    
    def pop(self):
        self.minStack.pop()
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]
    