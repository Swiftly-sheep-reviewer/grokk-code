def can_attend_all_appointments(intervals):
    """
    Given an array of intervals representing `n` appointments, find out if a
    person can attend all the appointments.

    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x[0])
    end = intervals[0][1]

    for interval in intervals[1:]:
        if interval[0] < end:
            return False
        end = interval[1]
    return True


def can_attend_all_appointments_sol(intervals):
    """
    Given an array of intervals representing `n` appointments, find out if a
    person can attend all the appointments.

    :param intervals:
    :return:
    """
    intervals.sort(key=lambda x: x[0])
    start, end = 0, 1
    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i-1][end]:
            return False
    return True




def main():
    print("Can attend all appointments: " + str(
        can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])))
    print("Can attend all appointments: " + str(
        can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])))
    print("Can attend all appointments: " + str(
        can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])))


if __name__ == "__main__":
    main()
