def count_rotations(arr):
    """
    Given an array of numbers which is sorted in asc order and is rotated `k`
    times around a pivot, find `k`.

    Args:
        arr: eg. [10, 15, 1, 3, 8]
    Returns:
        2. As the array has been rotated 2 times.
    """
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2

        # if mid is greater than the next element (than it's the max element)
        if mid < end and arr[mid] > arr[mid+1]:
            return mid+1
        # if mid is smaller than the previous element
        if mid > start and arr[mid] < arr[mid-1]:
            return mid

        # left side is sorted, so the pivot is on the right side
        if arr[start] < arr[mid]:
            start = mid+1
        # right side is sorted, so the pivot is on the left side
        else:
            end = mid-1
    # the array has not been rotated.
    return 0


def main():
    print(count_rotations([10, 15, 1, 3, 8]))
    print(count_rotations([4, 5, 7, 9, 10, -1, 2]))
    print(count_rotations([1, 3, 8, 10]))


if __name__ == "__main__":
    main()
