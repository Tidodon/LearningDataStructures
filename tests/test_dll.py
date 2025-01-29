import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/linkedList/")
import doublyLinkedList
import pytest

@pytest.fixture
def make_DLL():
    DLL = doublyLinkedList.DoublyLinkedList()
    return DLL

@pytest.fixture
def prep_DLL(make_DLL, lst=[5,6,7]):
    for num in lst:
        make_DLL.add(num)
    return make_DLL

class TestLinkedListMethods:

    def test_init(self, prep_DLL):
        assert bool(prep_DLL) is True

    def test_add(self, prep_DLL):
        assert prep_DLL.size == 3

    def test_peekFirst(self,prep_DLL):

        assert prep_DLL.head.data  == 5

    def test_peekLast(self,prep_DLL):

        assert prep_DLL.peekLast() == 7

    def test_head_tail(self,prep_DLL):

        assert prep_DLL.head.data == 5
        assert prep_DLL.tail.data == 7
        assert prep_DLL.tail.data == 7
        assert prep_DLL.head.prev == None
        assert prep_DLL.tail.next_ == None
        assert prep_DLL.head.next_ != None
        assert prep_DLL.tail.prev!= None

    def test_removeFirst(self,prep_DLL):

        prep_DLL.removeFirst()
        assert prep_DLL.peekFirst() == 6
        assert prep_DLL.head.data != 5
        assert prep_DLL.head.data == 6


    def test_removeLast(self,prep_DLL):

        prep_DLL.removeLast()
        assert prep_DLL.tail.data != 7
        assert prep_DLL.tail.data == 6

    def test_indexOf(self, prep_DLL):
        assert prep_DLL.indexOf(5) == 0
        assert prep_DLL.indexOf(6) == 1
        assert prep_DLL.indexOf(7) == 2

    def test_contains(self, prep_DLL):
        assert prep_DLL.contains(5) == True
        assert prep_DLL.contains(12) == False


    def test_removeValue(self, prep_DLL):
        prep_DLL.removeValue(6)
        assert prep_DLL.contains(6) == False
        assert prep_DLL.contains(5) == True
        assert prep_DLL.contains(7) == True
"""
        ####
    def test_removeAt(self, prep_DLL):

        prep_DLL.removeAt(1)
        assert prep_DLL.contains(6) == False
        assert prep_DLL.contains(5) == True
        assert prep_DLL.contains(7) == True

    def test_removeNode(self, prep_DLL):
        node_to_remove = prep_DLL.head.next_
        prep_DLL.removeNode(node_to_remove)
        assert prep_DLL.contains(6) == False
        assert prep_DLL.contains(5) == True
        assert prep_DLL.contains(7) == True

"""