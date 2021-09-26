from __future__ import print_function

from typing import List


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def merge(intervals: List[Interval]):
    """
    Given a list of intervals, merge all the overlapping intervals to produce
    a list that has only mutually exclusive intervals.

    :param intervals:
    :return:
    """
    merged = []
    intervals.sort(key=lambda x: x.start)

    start, end = intervals[0].start, intervals[0].end
    for interval in intervals[1:]:
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            merged.append(Interval(start, end))
            start = interval.start
            end = interval.end
    merged.append(Interval(start, end))
    return merged


def main():
    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 5), Interval(7, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(6, 7), Interval(2, 4), Interval(5, 9)]):
        i.print_interval()
    print()

    print("Merged intervals: ", end='')
    for i in merge([Interval(1, 4), Interval(2, 6), Interval(3, 5)]):
        i.print_interval()
    print()


if __name__ == "__main__":
    main()

