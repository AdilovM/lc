class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return None
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(r,c):
            q = deque([(r,c)])
            visited.add((r,c))
            directions = [[0,1], [0,-1],[1,0], [-1,0]]
            
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row,col) not in visited and row in range(ROWS) and col in range(COLS) and grid[row][col] == "1":
                        visited.add((row, col))
                        q.append((row, col))
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1
        return islands