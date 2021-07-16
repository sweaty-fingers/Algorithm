class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        queue = collections.deque([root])
        depth = 0
        while queue:
            depth += 1

            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return depth