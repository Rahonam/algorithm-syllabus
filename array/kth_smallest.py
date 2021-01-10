
def kth_smallest_using_sorting(arr: list, k: int):
    """
    Find K’th smallest element in the given array

    using: sorting, nlog(n) where n is len(arr)

    Args:
        arr: array of integers
        k: rank of the element to find
    
    Returns:
        integer: the K'th smallest element
    """

    arr.sort()
    return arr[k-1]


import heapq
class MaxHeap:

    def __init__(self, data=None):
        if data is None:
            self.data = []
        else:
            self.data = [-i for i in data]
            heapq.heapify(self.data)
    
    def top(self):
        return -self.data[0]
    
    def push(self, item):
        heapq.heappush(self.data, -item)
    
    def pop(self):
        return -heapq.heappop(self.data)
    
    def replace(self, item):
        return heapq.heapreplace(self.data, -item)


def kth_smallest_using_maxheap(arr: list, k: int):
    """
    Find K’th smallest element in the given array

    using: max heap, nlog(k) where n is len(arr)

    Args:
        arr: array of integers
        k: rank of the element to find
    
    Returns:
        integer: the K'th smallest element
    """

    #heap of size k
    heap = MaxHeap(arr[0: k])

    for i in range(k, len(arr)):
        #check if element is candidate to be among K smallest
        if arr[i] < heap.top():
            heap.replace(arr[i])

    return heap.top()


from heapq import heappop
def kth_smallest_using_minheap(arr: list, k: int):
    """
    Find K’th smallest element in the given array

    using: min heap, n+klog(n) where n is len(arr)

    Args:
        arr: array of integers
        k: rank of the element to find
    
    Returns:
        integer: the K'th smallest element
    """
    heapq.heapify(arr)
    
    for i in range(0, k -1):
        heappop(arr)

    return arr[0]


print(kth_smallest_using_sorting([7,4,6,3,9,1], 3))
print(kth_smallest_using_maxheap([7,4,6,3,9,1], 3))
print(kth_smallest_using_minheap([7,4,6,3,9,1], 3))