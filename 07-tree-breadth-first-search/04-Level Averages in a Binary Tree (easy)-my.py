from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_averages(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result
    queue = deque([root])
    while len(queue) > 0:
        level_sum = 0
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        result.append(level_sum / level_size)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))


main()
