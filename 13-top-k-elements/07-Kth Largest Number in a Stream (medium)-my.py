from heapq import *


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        # TODO: Write your code here
        self.k = k
        self.nums = nums
        self.min_heap = []
        for num in nums:
            heappush(self.min_heap, num)
            if len(self.min_heap) > self.k:
                heappop(self.min_heap)

    def add(self, num):
        # TODO: Write your code here
        heappush(self.min_heap, num)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]


def main():
    kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    print("4th largest number is: " + str(kthLargestNumber.add(6)))
    print("4th largest number is: " + str(kthLargestNumber.add(13)))
    print("4th largest number is: " + str(kthLargestNumber.add(4)))


main()
