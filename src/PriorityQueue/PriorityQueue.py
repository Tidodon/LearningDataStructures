


class PriorityQueue:

    def __init__(self):
        self.heapSize : int = 0
        self.heapCapacity : int = 0 
        self.heap = []
        self.Map = {}

    def PQueue1(self):
        self.heapCapacity  = 1

    def PQueueSize(self, sz : int):
        self.heapCapacity = sz
        self.heap = [None for val in range(sz)]
        
    def PQueueElems(self, elems : list):
        self.heapSize = self.heapCapacity = len(elems)
        self.heap = [None for _ in range(self.heapCapacity)]

        for i in range(self.heapSize):
            self.__mapAdd(elems[i],i)
            self.heap[i] = elems[i]

        for i in range( max([0, int(self.heapSize/2)-1]), -1 ,-1):
            self.__sink(i)

    def PQueueCol(self, elems):
        self.this(len(elems))
        for elem in elems:
            self.add(elem)

    
    def isEmpty(self):
        return self.heapSize == 0
 
    def clear(self):
        for i in range(self.heapCapacity):
            self.heap[i] = None
        self.heapSize = 0
        self.Map = {}               

    def size(self):
        return self.heapSize

    def peek(self):
        if self.isEmpty():
            return None
        return self.heap[0]
    
    def poll(self):
        return self.removeAt(0)
    
    def contains(self, elem):
        if elem == None:
            return False
        return self.map.containsKey(elem)

    def add(self, elem):
        if elem == None:
            raise Exception("Elem cannot be None")
        
        if self.heapSize < self.heapCapacity:
            self.heap[self.heapSize] = elem
        else:
            self.heap.append(elem)
            self.heapCapacity +=1
        
        self.__mapAdd(elem, self.heapSize)

        self.__swim(self.heapSize)
        self.heapSize +=1


    def __less(self, i, j):
        node1 = self.heap[i]
        node2 = self.heap[j]

        return (node1-node2) <= 0
    
    def __swim(self, k):
        parent = int((k-1)/2)

        while (k>0 and self.__less(k,parent)):
            self.__swap(parent,k)
            k = parent

            parent = int((k-1)/2)


    def __sink(self, k):

        while True:
            
            left  = 2 * k + 1
            right = 2 * k + 1
            smallest = left
            if (right < self.heapSize and self.__less(right,left)):
                smallest = right

            if (left >= self.heapSize or self.__less(k,smallest)):
                break
            
            self.__swap(smallest, k)
            k=smallest

    def __swap(self,i,j):
        i_elem = self.heap[i]
        j_elem = self.heap[j]

        self.heap[i] =  j_elem
        self.heap[j] =  i_elem

        self.__mapSwap(i_elem, j_elem, i ,j )

    def remove(self, elem):
        if elem == None:

            return False

        index = self.__mapGet(elem)
        if index != None:
            self.removeAt(index)
        return index != None

    def removeAt(self, i):

        if self.isEmpty():
            return None
        self.heapSize -= 1
        removed_data = self.heap[i]
        self.__swap(i,self.heapSize)

        self.heap[self.heapSize] == None
        self.__mapRemove(removed_data, self.heapSize)

        if (i ==self.heapSize):
            return removed_data
        
        elem = self.heap[i]

        self.__sink(i)

        if (self.heap[i] == elem):
            self.__swim(i)

        return removed_data
    
    def isMinHeap(self, k):
        if k>= self.heapSize:
            return True
        
        left = 2 * k + 1
        right = 2 * k + 2

        if (left < self.heapSize and not self.__less(k, left)):
            return False
        if (right < self.heapSize and not self.__less(k, right)):
            return False
        
        return self.isMinHeap(left) and self.isMinHeap(right)
    
    def __mapAdd(self, value, index):

        st = self.Map.get(value)
        if st == None:

            st = []
            st.append(index)
            self.Map[value] =  st

        else:
            st.append(index)

    def __mapRemove(self, value, index):
        st = self.Map[value]
        st.remove(index)
        if len(st) == 0:
            _ = self.Map.pop(value, None)

    def __mapGet(self, value):
        st = self.Map.get(value)
        if st is not None:
            return st[-1]
        return None
    
    def __mapSwap(self, val1, val2, val1Index, val2Index):
        st1 = self.Map[val1]
        st2 = self.Map[val2]

        st1.remove(val1Index)
        st2.remove(val2Index)

        st1.append(val2Index)
        st2.append(val1Index)

