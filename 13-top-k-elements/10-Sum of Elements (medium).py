from heapq import *


def find_sum_of_elements(nums, k1, k2):
    # TODO: Write your code here
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    count = 1
    while count <= k1:
        heappop(min_heap)
        count += 1
    total = 0
    while count < k2:
        total += heappop(min_heap)
        count += 1
    return total


def main():
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " +
          str(find_sum_of_elements([3, 5, 8, 7], 1, 4)))


main()
