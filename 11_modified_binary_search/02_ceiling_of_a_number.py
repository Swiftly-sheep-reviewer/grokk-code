def search_ceiling_of_a_number(arr, key):
    """

    :param arr: eg. [1,3,8,10,15]
    :param key: eg. 12
    :return:
    """
    n = len(arr)
    # if the key is bigger than the biggest element in the array
    if key > arr[n-1]:
        return -1

    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid-1
        elif key > arr[mid]:
            start = mid + 1
        else:  # found the key
            return mid
    # since the loop is running until `start <-= end`, so at the end of the
    # while loop, 
    return mid


def main():
    print(search_ceiling_of_a_number([4, 6, 10], 6))
    print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
    print(search_ceiling_of_a_number([4, 6, 10], 17))
    print(search_ceiling_of_a_number([4, 6, 10], -1))


if __name__ == "__main__":
    main()
