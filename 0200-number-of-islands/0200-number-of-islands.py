class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
        return 0
    
    # dimensions of grid
    rows, cols = len(grid), len(grid[0])
    # mark visited positions
    visited = set()
    # count num of islands
    islands = 0
    
    # bfs is not recursive, it is iterative so we need ds to use for memory. I'll use a queue
    def bfs(r,c):
        q = collections.deque()
        # mark as visited
        visited.add((r,c))
        # add to queue
        q.append((r,c))
        
        # while queue is not empty I'll continue expanding the island
        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1, 0], [0, 1], [0,-1]]
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visited:
                
                    # if that's true we need to run bfs on given cell
                    q.append((r, c))
                    visited.add((r,c))

    
    # every position in grid
    for r in range(rows):
        for c in range(cols):
            # if visited "1"
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r,c)
                islands += 1
    return islands




           