def binary_search(arr, key):
    """
    Returns the index of the key value in the array if there it is in the array.

    :param arr:
    :param key:
    :return:
    """
    # TODO: Write your code here
    start, end = 0, len(arr)-1
    is_asc = arr[start] < arr[end]

    while start <= end:
        # calculate the middle of the current range
        mid = (start + end) // 2
        if key == arr[mid]:
            return mid

        if is_asc:  # ascending order
            # key can be in the second half
            if key > arr[mid]:
                start = mid + 1
            # key can be in the first half
            else:
                end = mid - 1
        else:  # descending order
            # key can be in the first half
            if key > arr[mid]:
                end = mid - 1
            # key can be in the second half
            else:
                start = mid + 1
    return -1


def main():
    print(binary_search([4, 6, 10], 10))
    print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
    print(binary_search([10, 6, 4], 10))
    print(binary_search([10, 6, 4], 4))


if __name__ == "__main__":
    main()
