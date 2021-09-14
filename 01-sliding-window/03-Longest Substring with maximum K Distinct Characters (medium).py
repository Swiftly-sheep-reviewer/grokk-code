def longest_substring_with_k_distinct_my(str1, k):
    # TODO: Write your code here
    char_freq = dict()
    max_chars = 0
    start = 0
    for end in range(len(str1)):
        char_freq[str1[end]] = char_freq.get(str1[end], 0) + 1
        while len(char_freq) > k:
            letter = str1[start]
            char_freq[letter] -= 1
            if char_freq[letter] == 0:
                del char_freq[letter]
            start += 1
        max_chars = max(max_chars, end - start + 1)
    return max_chars


def longest_substring_with_k_distinct(str1, k):
    window_start = 0
    max_length = 0
    char_frequency = {}

    # in the following loop we'll try to extend the range
    # [window_start, window_end]
    for window_end in range(len(str1)):
        right_char = str1[window_end]
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1

        # shrink the sliding window, until we are left with 'k' distinct
        # characters in the char_frequency
        while len(char_frequency) > k:
            left_char = str1[window_start]
            char_frequency[left_char] -= 1
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            window_start += 1  # shrink the window
        # remember the maximum length so far
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: " + str(
        longest_substring_with_k_distinct("cbbebi", 3)))


main()
