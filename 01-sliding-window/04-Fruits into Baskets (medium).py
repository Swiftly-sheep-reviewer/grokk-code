def fruits_into_baskets_my(fruits):
    # TODO: Write your code here
    fruit_freq = dict()
    start = 0
    max_fruit = 0
    for end in range(len(fruits)):
        fruit = fruits[end]
        fruit_freq[fruit] = fruit_freq.get(fruit, 0) + 1
        while len(fruit_freq) > 2:
            left_fruit = fruits[start]
            fruit_freq[left_fruit] -= 1
            if fruit_freq[left_fruit] == 0:
                del fruit_freq[left_fruit]
            start += 1
        max_fruit = max(max_fruit, end - start + 1)
    return max_fruit


def fruits_into_baskets(fruits):
    window_start = 0
    max_length = 0
    fruit_frequency = {}

    # try to extend the range [window_start, window_end]
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1

        # shrink the sliding window, until we are left with '2' fruits in the fruit frequency dictionary
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            window_start += 1  # shrink the window
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def main():
    print("Maximum number of fruits: " + str(
        fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
    print("Maximum number of fruits: " + str(
        fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()
