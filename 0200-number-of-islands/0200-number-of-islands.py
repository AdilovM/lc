class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r,c):
            q = deque()            
            q.append((r,c))
            visited.add((r,c))
            directions = [[0,1], [0,-1], [1,0],[-1,0]]
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(ROWS) and col in range(COLS) and (row, col) not in visited and grid[row][col] == "1":
                        visited.add((row, col))
                        q.append((row, col))
                        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c] == "1":
                    bfs(r,c)
                    islands += 1
                    
        return islands
        
        