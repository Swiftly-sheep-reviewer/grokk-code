import random
from heapq import *


def find_kth_smallest_number_heap(nums, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, -nums[i])

    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])

    return -max_heap[0]


def find_kth_smallest_number_partition_scheme(nums, k):
    return find_kth_smallest_number_rec(nums, k, 0, len(nums)-1)


def find_kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k-1:
        return nums[p]
    if p > k-1:  # search lower part
        return find_kth_smallest_number_rec(nums, k, start, p-1)
    # search higher part
    return find_kth_smallest_number_rec(nums, k, p+1, end)


def partition(nums, low, high):
    if low == high:
        return low

    # use randomized pivot
    pivot_idx = random.randint(low, high)
    nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

    pivot = nums[high]
    for i in range(low, high):
        # all elements less than `pivot` will be before the index `low`
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
    # put the pivot in its correct place
    nums[low], nums[high] = nums[high], nums[low]
    return low


def median_of_medians(nums, low, high):
    """
    We use median of medians algorithm to choose a good pivot for the partition
    algorithm of the quicksort. it finds an approximate median of an array in
    linear time O(N).

    :param nums:
    :param low:
    :param high:
    :return:
    """
    n = high - low + 1
    # if we have less than 5 elements, ignore the partitioning algorithm
    if n < 5:
        return nums[low]

    # partition the given array into chunks of 5 elements
    partitions = [nums[j:j+5] for j in range(low, high+1, 5)]

    # for simplicity, lets ignore any partition with less than 5 elements
    full_partitions = [
        par for par in partitions if len(par) == 5
    ]

    # sort all partitions
    sorted_partitions = [sorted(par) for par in full_partitions]

    # find medians of all partitions; the median of each partition is at index 2
    medians = [par[2] for par in sorted_partitions]

    return partition(medians, 0, len(medians)-1)


def main():
    funcs = [
        find_kth_smallest_number_heap,
        find_kth_smallest_number_partition_scheme
    ]
    for func in funcs:
        print("Kth smallest number is: " + str(func([1, 5, 12, 2, 11, 5], 3)))

        # since there are two 5s in the input array, our 3rd and 4th smallest
        # numbers should be a '5'
        print("Kth smallest number is: " + str(func([1, 5, 12, 2, 11, 5], 4)))

        print("Kth smallest number is: " + str(func([5, 12, 11, -1, 12], 3)))


if __name__ == "__main__":
    main()
