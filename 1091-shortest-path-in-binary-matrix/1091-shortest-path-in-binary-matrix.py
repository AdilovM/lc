class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)])
        directions = [[0,1], [0,-1], [1,0], [-1,0],[1,1], [-1,-1], [1,-1], [-1,1]]
        visited = set((0,0))
        
        while q:
            r, c, length = q.popleft()
            if max(r,c) >= N or min(r,c) < 0 or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return length
            for dr, dc in directions:
                if (r + dr, c + dc) not in visited:
                    q.append((r + dr, c + dc, length + 1))
                    visited.add((r + dr, c + dc))
        return -1

                
        