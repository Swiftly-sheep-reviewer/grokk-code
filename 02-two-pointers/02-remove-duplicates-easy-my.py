def remove_duplicates(arr):
    # TODO: Write your code here
    next_non_duplicate = 1
    nxt = 1
    while nxt < len(arr):
        if arr[next_non_duplicate - 1] != arr[nxt]:
            arr[next_non_duplicate] = arr[nxt]
            next_non_duplicate += 1
        nxt += 1
    return next_non_duplicate


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


if __name__ == "__main__":
    main()
