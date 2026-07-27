"""
push - append val to the list
pop - pop from the list
top - return the last element added to the list
getMin - return the running min of the stack, or maintain a minStack 

Algo:

1. When pushing, compare the current val to the top of our minStack. If it's smaller, push to both stacks
2. When popping, compare the pop of the stack to the top of our minStack. If they're equal, pop from both.
3. Return last element of stack
4. Return the top of the minStack

["MinStack", "push", 1, "push", 2, "pop", "push", 5, "push", -1, "getMin"]
[1,5,-1]
mS: [1,-1]

"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1]
    
    def getMin(self) -> int:
        return self.minStack[-1]

