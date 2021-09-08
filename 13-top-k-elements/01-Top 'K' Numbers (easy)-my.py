from heapq import *


def find_k_largest_numbers(nums, k):
    result = []
    # TODO: Write your code here
    min_heap = []
    for i in range(k):
        heappush(min_heap, nums[i])
    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappush(min_heap, nums[i])
            heappop(min_heap)
    return min_heap


def main():
    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3)))

    print("Here are the top K numbers: " +
          str(find_k_largest_numbers([5, 12, 11, -1, 12], 3)))


main()
