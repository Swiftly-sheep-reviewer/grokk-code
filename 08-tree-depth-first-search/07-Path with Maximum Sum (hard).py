import math


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_maximum_path_sum(root):
    # TODO: Write your code here
    global_max_sum = [-math.inf]

    def dfs(node):
        if node is None:
            return 0
        max_sum_left = dfs(node.left)
        max_sum_right = dfs(node.right)
        max_sum_left = max(max_sum_left, 0)
        max_sum_right = max(max_sum_right, 0)
        local_max = max_sum_left + max_sum_right + node.val
        global_max_sum[0] = max(global_max_sum[0], local_max)
        return max(max_sum_left, max_sum_right) + node.val

    dfs(root)
    return global_max_sum[0]


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()
