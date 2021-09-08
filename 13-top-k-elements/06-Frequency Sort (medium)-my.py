from heapq import *


def sort_character_by_frequency(str):
    # TODO: Write your code here
    max_heap = []
    letter_freq = dict()
    for letter in str:
        letter_freq[letter] = letter_freq.get(letter, 0) + 1
    for letter, freq in letter_freq.items():
        heappush(max_heap, (-freq, letter))
    output = ""
    while max_heap:
        neg_freq, letter = heappop(max_heap)
        output += letter * (-neg_freq)

    return output


def main():
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
          sort_character_by_frequency("abcbab"))


main()
