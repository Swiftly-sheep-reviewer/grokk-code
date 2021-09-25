from typing import List


def search_min_diff_element(arr: List[int], key: int):
    """
    Given an array of numbers sorted in asc order, find the element in the array
    that has the minimum difference with the given `key`.

    :param arr:
    :param key:
    :return:
    """
    if key < arr[0]:
        return arr[0]
    n = len(arr)
    if key > arr[n-1]:
        return arr[n-1]

    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid-1
        elif key > arr[mid]:
            start = mid+1
        else:
            return arr[mid]

    # at the end of the while loop, `start == end+1`
    # we are not able to find the element in the given array
    # return the element which is closest to the `key`
    if arr[start] - key < key - arr[end]:
        return arr[start]
    return arr[end]


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


if __name__ == "__main__":
    main()
