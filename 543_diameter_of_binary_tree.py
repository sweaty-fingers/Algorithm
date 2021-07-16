class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node):

            if not node:
                return -1

            left = dfs(node.left)
            right = dfs(node.right)

            self.longest = max(self.longest, left + 1 + right + 1)

            return max(left, right) + 1

        dfs(root)

        return self.longest
