def insert(intervals, new_interval):
    """
    Given a list of non-overlapping intervals sorted by their start time, insert
    a given interval at the correct position and merge all necessary intervals
    to produce a list that has only mutually exclusive intervals.

    :param intervals: sorted
    :param new_interval:
    :return:
    """
    merged = []
    i = 0
    new_interval_start = new_interval[0]
    new_interval_end = new_interval[1]

    # skip intervals that has smaller end time than the new_interval
    while i < len(intervals) and intervals[i][1] < new_interval_start:
        merged.append(intervals[i])
        i += 1

    # merge overlapping intervals
    new_interval_start = min(new_interval_start, intervals[i][0])
    while i < len(intervals) and intervals[i][0] < new_interval_end:
        new_interval_end = max(new_interval_end, intervals[i][1])
        i += 1
    merged.append([new_interval_start, new_interval_end])

    # append the rest
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    return merged


def main():
    print("Intervals after inserting the new interval: " + str(
        insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(
        insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(
        insert([[2, 3], [5, 7]], [1, 4])))


if __name__ == "__main__":
    main()

"""
Time complexity #
As we are iterating through all the intervals only once, the time complexity of 
the above algorithm is O(N), where ‘N’ is the total number of intervals.

Space complexity #
The space complexity of the above algorithm will be O(N) as we need to return a 
list containing all the merged intervals.
"""