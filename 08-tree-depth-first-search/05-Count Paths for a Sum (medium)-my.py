class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    # TODO: Write your code here
    count = [0]

    def dfs(node, target_sum, current_path):
        if node is None:
            return 0
        current_path.append(node.val)
        path_count = 0
        path_sum = 0
        for i in range(len(current_path) - 1, -1, -1):
            path_sum += current_path[i]

            if path_sum == target_sum:
                path_count += 1
        path_count += dfs(node.left, target_sum, current_path)
        path_count += dfs(node.right, target_sum, current_path)
        del current_path[-1]
        return path_count

    return dfs(root, S, [])


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
