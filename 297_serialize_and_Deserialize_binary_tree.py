class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        
        queue = collections.deque([root])
        result = [str(root.val)]
        
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                    result.append(str(node.left.val))
                else:
                    result.append("#")
                    
                if node.right:
                    queue.append(node.right)
                    result.append(str(node.right.val))
                else:
                    result.append("#")

        
        return " ".join(result)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        if not data:
            return None
        
        data = data.split(" ")
        
        root = TreeNode(data.pop(0))
        queue = collections.deque([root])
        
        while data:
            for _ in range(len(queue)):
                node = queue.popleft()
                val = data.pop(0)
                    
                if val == '#':
                    pass
                else:
                    node.left = TreeNode(val)
                    queue.append(node.left)
                    
                val = data.pop(0)
                if val == "#":
                    pass
                else:
                    node.right = TreeNode(val)
                    queue.append(node.right)

        return root
        
        
        