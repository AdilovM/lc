class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # Helper function for DFS
        def dfs(node, parent):
            maxDistance, farthestNode = 0, node
            for neighbor in graph[node]:
                if neighbor != parent:
                    distance, nextNode = dfs(neighbor, node)
                    if distance > maxDistance:
                        maxDistance, farthestNode = distance, nextNode
            return maxDistance + 1, farthestNode

        # Step 2: First DFS to find the farthest node from an arbitrary start node (e.g., node 0)
        _, farthestNode = dfs(0, None)

        # Step 3: Second DFS to find the diameter
        diameter, _ = dfs(farthestNode, None)

        return diameter - 1