def search_bitonic_array(arr, key):
    """

    :param arr:
    :param key:
    :return:
    """
    max_idx = find_max(arr)
    key_idx = binary_search(arr, key, 0, max_idx)
    if key_idx != -1:
        return key_idx
    return binary_search(arr, key, max_idx + 1, len(arr) - 1)


# find index of the maximum value in a bitonic array
def find_max(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1
    # at the end of the while loop, `start == end`
    return start


def binary_search(arr, key, start, end):
    while start <= end:
        mid = (start + end) // 2

        if key == arr[mid]:
            return mid
        # ascending order
        if arr[start] < arr[end]:
            if key < arr[mid]:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if key < arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
    # element is not found
    return -1


def main():
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))


if __name__ == "__main__":
    main()

"""
Time complexity#
Since we are reducing the search range by half at every step, this means that 
the time complexity of our algorithm will be O(logN) where ‘N’ is the  total 
elements in the given array.

Space complexity#
The algorithm runs in constant space O(1).
"""