def calculate_bitwise_complement(num):
    """
    For a given positive number in base-10, return the complement of its binary
    representation as a base-10 integer.

    number ^ complement = all_bits_set
    number ^ number ^ complement = number ^ all_bits_set
    0 ^ complement = number ^ all_bits_set

    complement = number ^ all_bits_set

    :param num:
    :return:
    """
    # count number of total bits in `num`
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1

    # for a number which is a complete power of `2` i.e., it can be written as
    # pow(2, n), if we subtract `1` from such a number, we get a number which
    # has `n` least significant bits set to `1`.
    # For example, `4` which is a complete power of `2`, and `3` (which is one
    # less than 4) has a binary representation of `11` i.e., it has `2` least
    # significant bits set to `1`.
    all_bits_set = pow(2, bit_count) - 1

    # from the solution description: complement = number ^ all_bits_set
    return num ^ all_bits_set


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


if __name__ == "__main__":
    main()


"""
Time Complexity #
Time complexity of this solution is O(b) where ‘b’ is the number of bits 
required to store the given number.

Space Complexity #
Space complexity of this solution is O(1).
"""