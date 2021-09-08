from heapq import *


def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0
    min_heap = []
    # TODO: Write your code here
    for length in ropeLengths:
        heappush(min_heap, length)
    while len(min_heap) > 1:
        length1 = heappop(min_heap)
        length2 = heappop(min_heap)
        heappush(min_heap, length1+length2)
        result += length1 + length2

    return result


def main():
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([3, 4, 5, 6])))
    print("Minimum cost to connect ropes: " +
          str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2])))


main()
