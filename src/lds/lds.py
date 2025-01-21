class DynamicArray:
    def __init__(self):
        self.size   = 0
        self.capacity = 0
        self.arr       = []
        assert self.capacity >= 0, "Incorrect capacity value"

    def arrSize(self):
        return self.size

    def isEmpty(self) -> bool:
        return self.size==0 

    def get(self, index: int):
        return self.arr[index]

    def set(self, index: int, elem):
        self.arr[index] = elem

    def clear(self):
        for i in range(self.capacity):
            self.arr[i] = None
        self.size = 0

    def add(self, elem):
        if self.size+1 >= self.capacity: #5,5
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
            new_arr = [None for i in range(self.capacity)]
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr

            self.arr[self.size] = elem
            self.size +=1

    def removeAt(self, rm_index):
        assert rm_index < self.size and rm_index >= 0, "Incorrect rm_index"
        data = self.arr[rm_index]
        new_arr = [None for val in range(self.size-1)]
        j = 0
        for i in range(self.size): 
            if i == rm_index:
                continue
            new_arr[j] = self.arr[i]
            j += 1
        self.arr = new_arr
        self.capacity -= self.size
        return data

    def remove(self, elem):
        for i in range(self.size):
            if self.arr[i] == elem:
                self.removeAt(i)
                return True
        return False

    def indexOf(self, elem):
        for i in range(self.size):
            if self.arr[i] == elem:
                return i
        return -1

    def contains(self, elem):
        return self.indexOf(elem) != -1

    def hasNext(self,index):
        return index < self.size-1

    def next(self,index):
        return self.arr[index+1]

    def toString(self):
        if self.size==0:
            return "[]"
        else:
            t = "["
            for i in range(self.size):
                t += str(self.arr[i]) + ", "
            return t + "]"
        
if __name__ == "__main__":
    pass
