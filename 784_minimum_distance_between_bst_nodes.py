class Solution:
    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        def dfs(node):

            if node.left:
                dfs(node.left)

            self.result = min(self.result, node.val - self.prev)
            self.prev = node.val

            if node.right:
                dfs(node.right)

            return self.result

        return dfs(root)
