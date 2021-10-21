class Solution:
    longest = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node):

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if (
                node.left
                and node.right
                and node.val == node.left.val
                and node.val == node.right.val
            ):
                self.longest = max(self.longest, left + right + 2)
                return max(left, right) + 1

            if node.left and node.val == node.left.val:
                self.longest = max(self.longest, left + 1)
                return left + 1

            if node.right and node.val == node.right.val:
                self.longest = max(self.longest, right + 1)
                return right + 1

            return 0

        dfs(root)

        return self.longest