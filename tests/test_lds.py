import sys
sys.path.insert(0, "/Users/dbo/Documents/LearningDatastructures/src/lds/")
import lds

class TestLDS:
    test_arr = lds.DynamicArray()
    for i in [5,4,3,2]:
        test_arr.add(i)

    def test_arrSize(self):
        assert self.test_arr.arrSize() == 4
        #assert type(test_arr.arrSize()) == int

    def test_isEmpty(self):

        assert self.test_arr.isEmpty() == False

    def test_add(self):

        assert self.test_arr.arr == [5,4,3,2, None, None,None,None]

    def test_toString(self):

        assert self.test_arr.toString() == "[5, 4, 3, 2, ]"

    def test_contains(self):
        assert self.test_arr.contains(5) == True
        assert self.test_arr.contains(1) == False

    def test_size(self):
        assert self.test_arr.size == 4

    def test_size(self):
        assert self.test_arr.capacity == 8
