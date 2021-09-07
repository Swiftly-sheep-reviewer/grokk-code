from collections import defaultdict, deque


def find_order(tasks, prerequisites):
    sortedOrder = []
    # TODO: Write your code here
    in_degree = [0] * tasks
    graph = defaultdict(list)
    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        in_degree[child] += 1
        graph[parent].append(child)
    queue = deque()
    for i in range(len(in_degree)):
        if in_degree[i] == 0:
            queue.append(i)

    while len(queue) > 0:
        node = queue.popleft()
        sortedOrder.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)
    if len(sortedOrder) != tasks:
        return []
    return sortedOrder


def main():
    print("Is scheduling possible: " + str(find_order(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
          str(find_order(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
          str(find_order(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()