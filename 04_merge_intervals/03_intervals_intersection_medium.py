def merge(intervals_a, intervals_b):
    """
    Given two lists of intervals, find the intersection of these two lists. Each
    list consists of disjoint intervals sorted on their start time.

    :param intervals_a:
    :param intervals_b:
    :return:
    """
    result = []
    i, j, start, end = 0, 0, 0, 1

    while i < len(intervals_a) and j < len(intervals_b):
        if not (
            intervals_a[i][end] < intervals_b[j][start]
            or intervals_b[j][end] < intervals_a[i][start]
        ):
            result.append(
                [
                    max(intervals_a[i][start], intervals_b[j][start]),
                    min(intervals_a[i][end], intervals_b[j][end]),
                ]
            )
        if intervals_a[i][end] < intervals_b[j][end]:
            i += 1
        else:
            j += 1

    return result


def main():
    print(
        "Intervals Intersection: "
        + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]]))
    )
    print(
        "Intervals Intersection: "
        + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]]))
    )


if __name__ == "__main__":
    main()

"""
Time complexity #
As we are iterating through both the lists once, the time complexity of the 
above algorithm is O(N + M), where ‘N’ and ‘M’ are the total number of 
intervals in the input arrays respectively.

Space complexity #
Ignoring the space needed for the result list, the algorithm runs in constant 
space O(1).
"""