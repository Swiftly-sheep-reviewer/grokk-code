def find_single_number(arr):
    """
    In a non-empty array of integers, every number appears twice except for one,
    find that single number.

    :param arr:
    :return:
    """
    x1 = 0
    for num in arr:
        x1 = x1 ^ num
    return x1


def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))


if __name__ == "__main__":
    main()

