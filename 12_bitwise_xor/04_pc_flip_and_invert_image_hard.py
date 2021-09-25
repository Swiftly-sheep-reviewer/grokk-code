def flip_an_invert_image(matrix):
    n = len(matrix[0])
    for row in matrix:
        for i in range((n + 1) // 2):
            row[i], row[n - i - 1] = row[n - i - 1] ^ 1, row[i] ^ 1

    return matrix


def main():
    print(flip_an_invert_image([[1, 0, 1], [1, 1, 1], [0, 1, 1]]))
    print(flip_an_invert_image(
        [[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))


if __name__ == "__main__":
    main()


"""
Time Complexity#
The time complexity of this solution is O(n) as we iterate through all elements
of the input.

Space Complexity#
The space complexity of this solution is O(1).
"""