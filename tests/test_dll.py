import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/linkedList/")
import doublyLinkedList

class TestLinkedListMethods:
    DLL = doublyLinkedList.DoublyLinkedList()


    def test_init(self):
        assert bool(self.DLL) is True

    def test_add(self):
        self.DLL.add(5)
        assert self.DLL.size == 1
        assert self.DLL.head.data == self.DLL.tail.data

    def test_peekFirst(self):
        self.DLL.add(5)
        self.DLL.add(6)
        self.DLL.add(7)
        assert self.DLL.peekFirst() == 5

    def test_peekLast(self):
        self.DLL.add(5)
        self.DLL.add(6)
        self.DLL.add(7)
        assert self.DLL.peekLast() == 7

    def test_head_tail(self):
        self.DLL.add(5)
        self.DLL.add(6)
        self.DLL.add(7)
        assert self.DLL.head.data == 5
        assert self.DLL.tail.data == 7
        assert self.DLL.head.prev == None
        assert self.DLL.tail.next_ == None
        assert self.DLL.head.next_ != None
        assert self.DLL.tail.prev!= None



"""
    def test_removeFirst(self):
        self.DLL.add(5)
        self.DLL.add(6)
        self.DLL.add(7)
        self.DLL.removeFirst()
        assert self.DLL.head != 5
        assert self.DLL.head == 6

    def test_removeLast(self):
        self.DLL.add(5)
        self.DLL.add(6)
        self.DLL.add(7)
        self.DLL.removeLast()
        assert self.DLL.tail != 7
        assert self.DLL.tail == 6
"""