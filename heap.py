# Heap data structure is mainly used to represent a priority queue. 
# In Python, it is available using “heapq” module. The property of this data structure in Python is that each time the smallest of heap element is popped(min heap). 
# Whenever elements are pushed or popped, heap structure in maintained. 
# The heap[0] element also returns the smallest element each time. Let’s see various Operations on heap :

# heapify(iterable) :- This function is used to convert the iterable into a heap data structure. i.e. in heap order.
# heappush(heap, ele) :- This function is used to insert the element mentioned in its arguments into heap. 
# The order is adjusted, so as heap structure is maintained.
# heappop(heap) :- This function is used to remove and return the smallest element from heap. 
# The order is adjusted, so as heap structure is maintained.

# heappushpop(heap, ele) :- This function combines the functioning of both push and pop operations in one statement, increasing efficiency. 
# Heap order is maintained after this operation.
# heapreplace(heap, ele) :- This function also inserts and pops element in one statement, but it is different from above function. 
# In this, element is first popped, then the element is pushed.i.e, the value larger than the pushed value can be returned. 
# heapreplace() returns the smallest value originally in heap regardless of the pushed element as opposed to heappushpop().


import heapq
from sys import implementation

class solution:
    def implementingHeap(self,arr):
        heapq.heapify(arr)
        print("the heap is ", arr)

        heapq.heappush(arr,4)
        print("added element", arr)
        print("poped element",heapq.heappop(arr))

        return

if __name__ == "__main__":

    arr = [5, 7, 9, 1, 3]

    sol = solution()

    sol.implementingHeap(arr)
    