def find_letter_case_string_permutations(s: str):
    """

    :param s: example: "ad52"
    :return:
    """
    permutations = [s]
    # process every character of the string one by one
    for i in range(len(s)):
        # only process characters, skip digits
        if s[i].isalpha():
            # we will take all existing permutations and change the letter case
            # appropriately.
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                # if the current character is in upper case, change it to lower
                # case or vice versa
                chs[i] = chs[i].swapcase()
                permutations.append("".join(chs))

    return permutations


def main():
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
          str(find_letter_case_string_permutations("ab7c")))


if __name__ == "__main__":
    main()
