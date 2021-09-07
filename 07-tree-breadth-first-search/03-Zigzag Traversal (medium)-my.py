from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []
    # TODO: Write your code here
    if root is None:
        return result

    queue = deque([root])
    is_left_to_right = True
    while len(queue) > 0:
        level_list = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if is_left_to_right:
                level_list.append(node.val)
            else:
                level_list.appendleft(node.val)
            for child in [node.left, node.right]:
                if child:
                    queue.append(child)
        is_left_to_right = not is_left_to_right
        result.append(list(level_list))

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))


main()
