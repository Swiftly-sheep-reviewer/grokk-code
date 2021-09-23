from typing import List


def find_subsets(nums: List[int]):
    subsets = [[]]
    # start by adding empty subset

    for num in nums:
        # we will take all existing subsets and insert the current number in
        # them to create new subsets
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)

    return subsets


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


if __name__ == "__main__":
    main()
