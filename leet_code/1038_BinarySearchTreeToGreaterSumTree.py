# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maximum = 0

    def bstToGst(self, root: TreeNode) -> TreeNode:
        def dfs(node):

            if not node:
                return 0

            dfs(node.right)
            node.val = self.maximum + node.val
            self.maximum = node.val
            dfs(node.left)

            return

        dfs(root)

        return root
