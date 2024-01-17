class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def dfs(r, c, index):
            if (0 <= r < len(grid)) and (0 <= c < len(grid[0])) and grid[r][c] == 1:
                grid[r][c] = index  # Mark the island with a unique identifier
                return 1 + dfs(r+1, c, index) + dfs(r-1, c, index) + dfs(r, c+1, index) + dfs(r, c-1, index)
            return 0

        n = len(grid)
        index = 2  # Start from 2 because 0 and 1 are already used in the grid
        area = {0: 0}  # Dictionary to store area of each island by index

        # Identify and mark islands with unique index, calculate their areas
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    area[index] = dfs(r, c, index)
                    index += 1

        # Check if the grid has no island
        if not area: return 1

        # Evaluate the largest island that can be created by flipping one zero
        largest = max(area.values())  # The largest island without flipping
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = {grid[nr][nc] for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)] if 0 <= nr < n and 0 <= nc < n}
                    largest = max(largest, 1 + sum(area[i] for i in seen))

        return largest
