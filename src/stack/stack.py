from collections import deque


class Stack:

    def __init__(self):
        self.Stack = deque()
        
    def addElem(self, elem):
        self.Stack.appendleft(elem)

    def size(self):
        return len([val for val in self.Stack])

    def isEmpty(self):
        return self.size() == 0
    
    def push(self, elem):
        self.Stack.appendleft(elem)

    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        self.Stack.popleft()

    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        return self.Stack[0]
    