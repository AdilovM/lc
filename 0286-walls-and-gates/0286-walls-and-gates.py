class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return

        rows, cols = len(rooms), len(rooms[0])
        gates = [(i, j) for i in range(rows) for j in range(cols) if rooms[i][j] == 0]

        def bfs():
            queue = deque(gates)
            while queue:
                row, col = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == 2147483647:
                        rooms[r][c] = rooms[row][col] + 1
                        queue.append((r, c))

        bfs()