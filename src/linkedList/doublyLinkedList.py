
import copy

class DoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def clear(self) -> None:
        trav = self.head
        while trav != None:
            next_ = trav.next_
            trav.prev = None
            trav.next_ = None
            trav.data = None
            trav = next_
        self.head = None
        self.tail = None
        trav = None
        self.size = 0

    def size(self) -> int: 
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def add(self, elem):
        self.addLast(elem)

    def addFirst(self, elem):
        if self.isEmpty():
            self.head = Node(data=elem, prev=None, next_=None )
            self.tail = Node(data=elem, prev=None, next_=None )
        else: 
            self.head.prev = Node( data=elem, prev=None, next_=self.head)
            self.head = self.head.prev
        self.size += 1

    def addLast(self, elem):
        if self.isEmpty():
            self.head = self.tail = Node(data=elem, prev=None, next_=None)
            
        else: 
            self.tail.next_ = Node(data=elem, prev=self.tail, next_=None)
            self.tail = self.tail.next_
        self.size += 1

    def peekFirst(self):
        if self.isEmpty():
            raise Exception("Empty List")
        return self.head.data

    def peekLast(self):
        if self.isEmpty():
            raise Exception("Empty List")
        return self.tail.data
    
    def removeFirst(self):
        if self.isEmpty():
            raise Exception("Empty List")

        data = self.head.data
        self.head = self.head.next_
        self.size -= 1

        if self.isEmpty():
            self.tail = None
        else:
            self.head.prev = None

        return data

    def removeLast(self):
        if self.isEmpty():
            raise Exception("Empty List")

        data = self.tail.data
        self.tail = self.tail.prev
        self.size -= 1

        if self.isEmpty():
            self.head = None
        else:
            self.tail.next_ = None

        return data

    def removeNode(self, node):
        if node.prev == None:
            return self.removeFirst()
        if node.next_ == None:
            return self.removeLast()

        node.next_.prev = node.prev
        node.prev.next_ = node.next_

        data = node.data

        node.data = None
        node, node.prev, node.next_ = None

        self.size -= 1

        return data

    def removeAt(self, index):
        if (index < 0 | index >= self.size):
            raise Exception("Invalid Index")

        
        if index < int(self.size/2):
            trav = self.head
            for i in range(self.size):
                if i == index:
                    break
                trav = trav.next_
        else:
            trav = self.tail
            for i in range(self.size-1, -1, -1):
                if i == index:
                    break
                trav = trav.prev

        return self.removeNode(trav)

    def removeValue(self, obj):
        trav=self.head
        if obj == None:
            while trav != None:
                if trav.data == None:
                    self.remove(trav)
                    return True
                trav = trav.next_
        else:
            while trav != None:
                if trav.data == obj:
                    self.remove(trav)
                    return True
            trav = trav.next_

        return False

    def indexOf(self, obj):
        index = 0
        trav = self.head

        if obj== None:
            while trav != None:
                if obj == trav.data:
                    return index
                trav = trav.next_
                index +=1
        else:
            while trav != None:
                if obj == trav.data:
                    return index
                trav = trav.next_
                index +=1
        return -1

    def contains(self, obj):
        return self.indexOf(obj) != -1

    def toString(self):
        sb = ""
        sb += ("[ ")
        trav = self.head

        while trav != None:
            sb += str(trav.data) + ", "
            trav=trav.next_
        sb += " ]"
        return sb



class Node:

    def __init__(self, data=None, prev = None , next_=None):
        self.data = data
        self.prev = prev
        self.next_ = next_

