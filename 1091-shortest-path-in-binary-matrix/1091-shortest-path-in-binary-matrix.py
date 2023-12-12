class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        q = deque([(0,0,1)]) # r,c,length
        visited = set((0,0))
        directions = [[0,1], [0,-1], [1,0], [-1,0],[1,1], [-1,-1], [1,-1], [-1,1]]

        while q:
            current_row, current_column, length = q.popleft()
            if (min(current_row,current_column) < 0 or max(current_row,current_column) >= N or grid[current_row][current_column] == 1):
                continue
            if current_row == N - 1 and current_column == N - 1:
                return length
            for dr, dc in directions:
                if (current_row + dr, current_column + dc) not in visited:
                    q.append((current_row + dr, current_column + dc, length + 1))
                    visited.add((current_row + dr, current_column + dc))
        return -1

                
        