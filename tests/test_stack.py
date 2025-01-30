
import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/stack/")
import stack
import pytest

@pytest.fixture
def init_stack():
    s = stack.Stack()
    return s

class TestStackClass:


    def test_size(self, init_stack):
        assert init_stack.size() == 0

    def test_init_empty(self, init_stack):
        assert init_stack.isEmpty() == True

    def test_addElem(self, init_stack):
        assert init_stack.size() == 0

    def test_push(self, init_stack):
        init_stack.addElem(5)
        init_stack.addElem(7)
        init_stack.addElem("a")
        assert init_stack.size() == 3
        assert init_stack.Stack[0] == "a"
        assert init_stack.Stack[2] == 5

    def test_pop(self, init_stack):

        init_stack.addElem(5)
        init_stack.addElem(7)
        init_stack.addElem("a")
        init_stack.pop()
        assert init_stack.Stack[0] == 7
        init_stack.pop()
        init_stack.pop()
        with pytest.raises(Exception) as ex_info:
            init_stack.pop() 

    def test_peek(self, init_stack):
        init_stack.addElem(5)
        init_stack.addElem(7)
        init_stack.addElem("a")
        assert init_stack.peek() == "a"
        init_stack.pop()
        assert init_stack.peek() == 7


