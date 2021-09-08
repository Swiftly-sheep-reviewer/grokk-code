from heapq import *


def find_k_frequent_numbers(nums, k):
    topNumbers = []
    min_heap = []
    num_dict = dict()
    # TODO: Write your code here
    for num in nums:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    for num, freq in num_dict.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)
    return [t[1] for t in min_heap]


def main():
    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))

    print("Here are the K frequent numbers: " +
          str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))


main()
