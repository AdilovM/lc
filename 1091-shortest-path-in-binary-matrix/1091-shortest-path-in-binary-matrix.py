class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        # deque will store set of r,c and current depth
        q = deque([(0,0,1)])
        # hashset of visited cell
        visited = set((0,0))
        # 8 directions in form of r and c
        directions = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        while q:
            r, c, d = q.popleft()
            if max(r,c) >= N or min(r,c) < 0 or grid[r][c] == 1:
                continue
            if r == N - 1 and c == N - 1:
                return d
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (row, col) not in visited:
                    visited.add((row,col))
                    q.append((row,col,d + 1))
        return -1