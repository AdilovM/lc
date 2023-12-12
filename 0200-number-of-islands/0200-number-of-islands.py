class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        
        
        def dfs(r,c):
            if (r,c) in visited or r not in range(ROWS) or c not in range(COLS) or grid[r][c] == "0":
                return
            visited.add((r,c))
            for dr, dc in directions:
                row = r + dr
                col = c + dc
                dfs(row, col)
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    islands += 1
                    dfs(r,c)
        return islands