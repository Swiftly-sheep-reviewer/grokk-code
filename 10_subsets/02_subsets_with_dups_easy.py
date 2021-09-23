from typing import List


def subsets_with_dups(nums: List[int]):
    """
    Given a set of numbers that might contain duplicates, find all of its
    distinct subsets.
    :param nums:
    :return:
    """
    nums.sort()
    subsets = [[]]
    start_idx, end_idx = 0, 0

    for i in range(len(nums)):
        start_idx = 0
        # if current and previous elements are the same, create new subsets only
        # from subsets added in previous steps
        if i > 0 and nums[i] == nums[i - 1]:
            start_idx = end_idx + 1
        end_idx = len(subsets) - 1
        for j in range(start_idx, end_idx + 1):
            # create a new subset from the existing subset and add the current
            # element to it
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


def main():
    print("Here is the list of subsets: " + str(subsets_with_dups([1, 3, 3])))
    print("Here is the list of subsets: " + str(subsets_with_dups([1, 5, 3, 3])))


if __name__ == "__main__":
    main()
