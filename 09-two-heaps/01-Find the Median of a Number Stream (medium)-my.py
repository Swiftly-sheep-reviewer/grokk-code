from heapq import *


class MedianOfAStream:

    def __init__(self):
        # store smaller half
        self.max_heap = []
        # store bigger half
        self.min_heap = []

    def insert_num(self, num):
        # TODO: Write your code here
        if len(self.max_heap) == 0 or self.max_heap[0] < -num:
            heappush(self.max_heap, -num)
        else:
            heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            heappush(self.min_heap, -heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heappush(self.max_heap, -heappop(self.min_heap))
        return -1

    def find_median(self):
        # TODO: Write your code here
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


def main():
    medianOfAStream = MedianOfAStream()
    medianOfAStream.insert_num(3)
    medianOfAStream.insert_num(1)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(5)
    print("The median is: " + str(medianOfAStream.find_median()))
    medianOfAStream.insert_num(4)
    print("The median is: " + str(medianOfAStream.find_median()))


main()
