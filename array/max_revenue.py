
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


def max_revenue(arr: list, k: int):
    """
    Find maximum revenue by selling K tickets from N windows, Price of a ticket is equal to number of tickets remaining at that window

    using: max heap, time O(klog(n))

    Args:
        arr: array of integers
        k: number of tickets to be sold
    
    Returns:
        integer: the maximum revenue
    """
    heap = MaxHeap(arr)
    revenue = 0

    for i in range(0, k):
        current_max = heap.top()
        revenue += heap.pop()
        heap.push(current_max - 1)

    return revenue


print(max_revenue([5, 1, 7, 10, 11, 9], 4))
print(max_revenue([5, 1, 7, 10, 11, 9], 5))