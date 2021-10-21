class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        if not root:
            return

        queue = collections.deque([root])

        while queue:

            for _ in range(len(queue)):
                node = queue.popleft()

                node.right, node.left = node.left, node.right

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root