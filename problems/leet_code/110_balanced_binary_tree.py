class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1 or left == -1 or right == -1:
                return -1

            return max(left, right) + 1

        return dfs(root) != -1