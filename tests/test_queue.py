import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/MyQueue/")
import MyQueue
import pytest

@pytest.fixture
def q():
    q = MyQueue.MyQueue()
    q.offer(5)
    return q


class TestQueue:


    def test_size(self, q):
        assert q.size() == 1

    def test_isEmpty(self,q):
        assert q.isEmpty() == False

    def test_peek(self,q):
        assert q.peek() == 5

    def test_poll(self,q):
        q.poll()
        assert q.size() == 0
        assert q.isEmpty() == True
        q.offer(4)
        q.offer(5)
        q.offer(6)
        assert q.size() == 3
        assert q.isEmpty() == False
        q.poll()
        assert q.size() == 2
        assert q.isEmpty() == False
        assert q.peek() == 5

    def test_offer(self,q):
        q.offer(4)
        q.offer("abs")
        q.offer(None)
        assert q.size() == 4