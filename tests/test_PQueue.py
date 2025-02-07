
import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/PriorityQueue/")
import PriorityQueue
import pytest

@pytest.fixture
def a():
    a = PriorityQueue.PriorityQueue()
    for val in range(1,5):
        a.add(val)
    
    return a

class TestPriorityQueue:

    def test_init_queue(self,a ):
        assert a.heapSize == 4
        assert a.heapSize == a.heapCapacity
        assert a.heap[0] == 1
        assert a.Map[1] == [0]
        assert a.Map[4] == [3]

    def test_isEmpty(self, a ):
        assert a.isEmpty() == False

    def test_clear(self, a):
        a.clear()
        assert a.heapSize == 0
        assert any(a.heap) == False

    def test_peek(self, a):
        assert a.peek() == 1
        a.clear()
        assert a.peek() == None

    def test_poll(self,a):
        assert a.heap[0] == 1
        a.poll()
        assert a.heapSize == 3
        assert a.Map.get(1) == None
        assert a.heap[0] == 2
        assert a.heap[1] == 4
        assert a.heap[2] == 3

    def test_remove(self, a):
        assert a.heap[3] == 4
        a.remove(3)
        assert a.Map.get(3) == None

    def test_isMinHeap(self, a):
        assert a.isMinHeap(2) == True
