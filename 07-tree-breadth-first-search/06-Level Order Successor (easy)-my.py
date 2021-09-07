from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_successor(root, key):
    # TODO: Write your code here
    if root is None:
        return None
    queue = deque([root])
    while len(queue) > 0:
        for _ in range(len(queue)):
            node = queue.popleft()
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
            if node.val == key:
                return queue[0] if len(queue) > 0 else None
    return None


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.val)
    result = find_successor(root, 9)
    if result:
        print(result.val)


main()
