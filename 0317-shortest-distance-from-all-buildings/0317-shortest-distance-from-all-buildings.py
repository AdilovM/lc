class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        rows, cols = len(grid), len(grid[0])
        dist_sum = [[0] * cols for _ in range(rows)] # Total distance sum to all buildings
        reachable_count = [[0] * cols for _ in range(rows)] # Count of reachable buildings

        def bfs(start_r, start_c):
            visited = [[False] * cols for _ in range(rows)]
            visited[start_r][start_c] = True
            queue = deque([(start_r, start_c, 0)]) # Queue for BFS: (row, col, distance)

            while queue:
                r, c, dist = queue.popleft()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == 0:
                        visited[nr][nc] = True
                        dist_sum[nr][nc] += dist + 1
                        reachable_count[nr][nc] += 1
                        queue.append((nr, nc, dist + 1))

        building_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    building_count += 1
                    bfs(r, c)

        min_dist = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reachable_count[r][c] == building_count:
                    min_dist = min(min_dist, dist_sum[r][c])

        return min_dist if min_dist != float('inf') else -1