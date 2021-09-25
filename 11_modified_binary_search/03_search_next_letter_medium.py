from typing import List


def search_next_letter(letters: List[str], key: str) -> str:
    """
    Assume the array is a `circular list`, meaning that the latst letter is
    connected with the first letter. Find the smallest letter in the given list
    greater than a given `key`

    Args:
        letters (List[str]): a list of unique english characters
        key: a english character
    Returns:
        smallest letter in the list that is greater than the given `key`.
    """
    n = len(letters)

    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if key < letters[mid]:
            end = mid-1
        else:  # key >= letters[mid]
            start = mid + 1
    # since the loop is running until `start <= end`, so at the end of the while
    # loop, `start == end+1`
    return letters[start % n]


def main():
    funcs = [search_next_letter]
    for func in funcs:
        print(func(['a', 'c', 'f', 'h'], 'f'))
        print(func(['a', 'c', 'f', 'h'], 'b'))
        print(func(['a', 'c', 'f', 'h'], 'm'))


if __name__ == "__main__":
    main()
