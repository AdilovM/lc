class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:  # Check for the correct number of edges
            return False

        # Create an adjacency list
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # DFS to check for cycles and if the graph is connected
        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:  # Ignore the immediate parent
                    continue
                if neighbor in visited:  # Found a cycle
                    return False
                if not dfs(neighbor, node):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check if all nodes are visited (graph is connected)
        return len(visited) == n