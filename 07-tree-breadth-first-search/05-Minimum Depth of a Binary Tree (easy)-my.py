from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):
    # TODO: Write your code here
    if root is None:
        return 0
    queue = deque([root])
    depth = 0
    while len(queue) > 0:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left is None and node.right is None:
                return depth
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)

    return depth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
