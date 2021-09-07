from collections import defaultdict, deque


def print_orders(tasks, prerequisites):
    # TODO: Write your code here
    sorted_order = []
    in_degree = [0] * tasks
    graph = defaultdict(list)

    for pre in prerequisites:
        parent, child = pre[0], pre[1]
        graph[parent].append(child)
        in_degree[child] += 1

    sources = deque()
    for child in range(len(in_degree)):
        if in_degree[child] == 0:
            sources.append(child)

    print_all_top_sorts(in_degree, graph, sources, sorted_order)

def print_all_top_sorts(in_degree, graph, sources, sorted_order):
    if sources:
        for vertex in sources:
            sorted_order.append(vertex)
            sources_for_next_call = deque(sources)
            sources_for_next_call.remove(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    sources_for_next_call.append(child)

            print_all_top_sorts(
                in_degree=in_degree,
                graph=graph,
                sources=sources_for_next_call,
                sorted_order=sorted_order
            )

            sorted_order.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1
    if len(sorted_order) == len(in_degree):
        print(sorted_order)


def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])


if __name__ == "__main__":
    main()
