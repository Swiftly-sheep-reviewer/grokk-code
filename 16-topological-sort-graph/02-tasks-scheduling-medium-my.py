from collections import defaultdict, deque

def is_scheduling_possible(tasks, prerequisites):
  # TODO: Write your code here
  in_degree = [0] * tasks
  graph = defaultdict(list)
  ordered = []
  for prereq in prerequisites:
        parent, child = prereq[0], prereq[1]
        graph[parent].append(child)
        in_degree[child] += 1
  queue = deque()
  for i in range(len(in_degree)):
        if in_degree[i] == 0:
              queue.append(i)
  while len(queue) > 0:
        node = queue.popleft()
        ordered.append(node)
        for child in graph[node]:
              in_degree[child] -= 1
              if in_degree[child] == 0:
                    queue.append(child)

  return len(ordered) == tasks


def main():
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
  print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()