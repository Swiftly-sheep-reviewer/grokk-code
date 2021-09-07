from heapq import *


def find_kth_smallest(lists, k):
    min_heap = []

    # put the 1st element of each list in the min_heap
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], 0, lists[i]))
    count = 1
    number = 0
    while min_heap:
        num, idx, lst = heappop(min_heap)
        if count == k:
            number = num
        if idx < len(lst)-1:
            heappush(min_heap, (lst[idx+1], idx+1, lst))
        count += 1

    return number


def main():
    print("Kth smallest number is: " +
          str(find_kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


if __name__ == "__main__":
    main()
