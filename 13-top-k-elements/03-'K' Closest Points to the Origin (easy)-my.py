from heapq import *


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')


def find_closest_points(points, k):
    result = []
    max_heap = []

    # TODO: Write your code here
    def get_dist(point: Point):
        return point.x ** 2 + point.y ** 2

    for i in range(k):
        heappush(max_heap, (-get_dist(points[i]), points[i]))
    for i in range(k, len(points)):
        if -max_heap[0][0] > (get_dist(points[i])):
            heappush(max_heap, (-get_dist(points[i]), points[i]))
            heappop(max_heap)
    return [t[1] for t in max_heap]


def main():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    print("Here are the k points closest the origin: ", end='')
    for point in result:
        point.print_point()


main()
