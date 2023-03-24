"""
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
"""

class stack():
    def __init__(self):
        self.stackStore = []
    
    def push(self,val):
        self.stackStore.insert(0,val)

    def pop(self):
        if len(self.stackStore) == 0:
            return print('There are no elements in the stack')
        if len(self.stackStore) > 0:
            return self.stackStore.pop(0)
    
    def max(self):
        if len(self.stackStore) == 0:
            return print('There are no elements in the stack')
        if len(self.stackStore) > 0:
            return max(self.stackStore)

    def list(self):
        return print(self.stackStore)