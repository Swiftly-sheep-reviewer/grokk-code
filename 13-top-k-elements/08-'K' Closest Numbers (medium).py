from heapq import *


def find_closest_elements(arr, K, X):
    result = []
    max_heap = []
    # TODO: Write your code here
    for i in range(K):
        heappush(max_heap, (-abs(arr[i]-X), arr[i]))
    for i in range(K, len(arr)):
        if -max_heap[0][0] > abs(arr[i]-X):
            heappush(max_heap, (-abs(arr[i]-X), arr[i]))
            heappop(max_heap)
    return [t[1] for t in max_heap]


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
