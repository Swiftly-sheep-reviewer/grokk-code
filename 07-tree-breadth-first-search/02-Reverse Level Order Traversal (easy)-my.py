from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    # TODO: Write your code here
    if root is None:
        return result
    queue = deque([root])
    while len(queue) > 0:
        level_list = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_list.append(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        result.appendleft(level_list)

    return list(result)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


if __name__ == '__main__':
    main()
