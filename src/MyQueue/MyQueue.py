from collections import deque

class MyQueue:

    def __init__(self):
        self.Queue = deque()

    def size(self):
       return len([val for val in self.Queue])
    
    def isEmpty(self):
        return self.size() == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.Queue[0]
    
    def poll(self):
        if self.isEmpty():
            raise Exception("Queue is empty")
        return self.Queue.popleft()
    
    def offer(self, elem):
        self.Queue.append(elem)