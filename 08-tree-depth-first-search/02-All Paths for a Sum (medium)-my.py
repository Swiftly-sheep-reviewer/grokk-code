class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_paths(root, sum):
    allPaths = []

    # TODO: Write your code here
    def dfs(node, sum_target, path):
        if node is None:
            return
        path.append(node.val)
        if node.val == sum_target and node.left is None and node.right is None:
            allPaths.append(list(path))
        dfs(node.left, sum_target - node.val, path)
        dfs(node.right, sum_target - node.val, path)
        del path[-1]

    dfs(root, sum, [])
    return allPaths


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
