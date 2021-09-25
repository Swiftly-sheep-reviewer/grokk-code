from typing import List


def find_range(arr: List[int], key: int):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    if result[0] != -1:
        result[1] = binary_search(arr, key, True)
    return result


def binary_search(arr: List[int], key: int, find_max_index: bool):
    key_index = -1
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if key < arr[mid]:
            end = mid - 1
        elif key > arr[mid]:
            start = mid + 1
        # key == arr[mid
        else:
            key_index = mid
            if find_max_index:
                start = mid + 1
            else:
                end = mid - 1
    return key_index


def main():
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))


if __name__ == "__main__":
    main()
