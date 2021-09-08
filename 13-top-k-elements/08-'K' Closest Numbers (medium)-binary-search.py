from heapq import *

def find_closest_elements(arr, K, X):
    result = []
    # TODO: Write your code here
    idx = binary_search(arr, X)
    low = idx - K
    high = idx + K
    low = max(low, 0)
    high = min(high, len(arr)-1)

    min_heap = []
    for i in range(low, high+1):
        heappush(min_heap, (abs(arr[i]-X), arr[i]))

    for i in range(K):
        result.append(heappop(min_heap)[1])

    result.sort()
    return result


def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    if low > 0:
        return low - 1
    return low


def main():
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("'K' closest numbers to 'X' are: " +
          str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))


main()
