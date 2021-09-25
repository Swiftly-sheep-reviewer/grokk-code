"""
XOR is a logical bitwise operator that returns 0 (false) if both bits are the
same and returns 1 (true) otherwise.
In other words, it only returns 1 if exactly one bit is set to 1 out of the two
bits in comparison.
"""
# |   A   |   B   |   A xor B |
# |   0   |   0   |   0       |
# |   0   |   1   |   1       |
# |   1   |   0   |   1       |
# |   1   |   1   |   0       |

"""
Important properties:

1 ^ 1 = 0
29 ^ 29 = 0

1 ^ 0 = 1
21 ^ 0 = 21

(a ^ b) ^ c = a ^ (b ^ c)
a ^ b = b ^ a
"""

"""
Given an array of n-1 integers in the range from 1 to n, find the one number 
that is missing from the array.
"""


def find_missing_number(arr):
    n = len(arr) + 1
    # find sum of all numbers from 1 to n.
    s1 = 0
    for i in range(1, n + 1):
        s1 += i

    # subtract all numbers in input from sum.
    for i in arr:
        s1 -= i

    # s1, now, is the missing number
    return s1


def find_missing_number_xor(arr):
    n = len(arr) + 1
    # x1 represent XOR of all values from 1 to n
    x1 = 1
    for i in range(2, n+1):
        x1 = x1 ^ i

    # x2 represents XOR of all values in arr
    x2 = arr[0]
    for i in range(1, n-1):
        x2 = x2 ^ arr[i]

    # missing number is the xor of x1 and x2
    return x1 ^ x2


def main():
    arr = [1, 5, 2, 6, 4]
    funcs = [find_missing_number, find_missing_number_xor]
    for func in funcs:
        print('Missing number is:' + str(func(arr)))


if __name__ == "__main__":
    main()
