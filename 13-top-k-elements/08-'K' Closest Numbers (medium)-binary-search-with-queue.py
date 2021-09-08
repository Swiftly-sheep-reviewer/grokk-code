from collections import deque


def find_closest_elements(arr, K, X):
    result = deque()
    index = binary_search(arr, X)
    leftPointer, rightPointer = index, index + 1
    n = len(arr)
    for i in range(K):
        if leftPointer >= 0 and rightPointer < n:
            diff1 = abs(X - arr[leftPointer])
            diff2 = abs(X - arr[rightPointer])
            if diff1 <= diff2:
                result.appendleft(arr[leftPointer])
                leftPointer -= 1
            else:
                result.append(arr[rightPointer])
                rightPointer += 1
        elif leftPointer >= 0:
            result.appendleft(arr[leftPointer])
            leftPointer -= 1
        elif rightPointer < n:
            result.append(arr[rightPointer])
            rightPointer += 1

    return result


def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
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
