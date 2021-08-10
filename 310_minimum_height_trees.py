class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n == 1:
            return [0]

        graph = collections.defaultdict(list)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        leaves = []
        new_leaves = []

        for i in graph.keys():
            if len(graph[i]) == 1:
                new_leaves.append(i)

        leaves = new_leaves[:]

        while n > 2:
            n -= len(leaves)
            new_leaves = []

            for i in leaves:
                j = graph[i].pop()
                graph[j].remove(i)

                if len(graph[j]) == 1:
                    new_leaves.append(j)

            leaves = new_leaves[:]

        return leaves
