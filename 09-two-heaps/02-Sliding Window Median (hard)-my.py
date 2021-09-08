import heapq
from heapq import *


class SlidingWindowMedian:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def find_sliding_window_median(self, nums, k):
        result = [0.0] * (len(nums)-k+1)
        # TODO: Write your code here
        for i in range(len(nums)):
            if len(self.max_heap) == 0 or self.max_heap[0] < -nums[i]:
                heappush(self.max_heap, -nums[i])
            else:
                heappush(self.min_heap, nums[i])
            self.rebalance_heaps()
            if i-k+1 >= 0:
                if len(self.max_heap) == len(self.min_heap):
                    result[i-k+1] = (self.min_heap[0] - self.max_heap[0])/2
                else:
                    result[i-k+1] = -self.max_heap[0] / 1
                remove_element = nums[i-k+1]
                if remove_element <= -self.max_heap[0]:
                    self.remove(self.max_heap, -remove_element)
                else:
                    self.remove(self.min_heap, remove_element)
            self.rebalance_heaps()

        return result

    def remove(self, heap, element):
        idx = heap.index(element)
        heap[idx] = heap[-1]
        del heap[-1]
        if idx < len(heap):
            heapq._siftup(heap, idx)
            heapq._siftdown(heap, 0, idx)

    def rebalance_heaps(self):
        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))

def main():
    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    slidingWindowMedian = SlidingWindowMedian()
    result = slidingWindowMedian.find_sliding_window_median(
        [1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()
