from collections import deque


def generate_permutations(nums):
    nums_len = len(nums)
    result = []
    permutations = deque()
    permutations.append([])
    for num in nums:
        # we will take all existing permutation and add the current number to
        # create new permutations
        n = len(permutations)
        for _ in range(n):
            old_perm = permutations.popleft()
            # create a new permutation by adding the current number at every
            # position (index)
            for j in range(len(old_perm)+1):
                new_prem = list(old_perm)
                new_prem.insert(j, num)
                if len(new_prem) == nums_len:
                    result.append(new_prem)
                else:
                    permutations.append(new_prem)
    return result


def main():
    print("Here are all the permutations: " + str(
        generate_permutations([1, 3, 5])))


if __name__ == "__main__":
    main()
