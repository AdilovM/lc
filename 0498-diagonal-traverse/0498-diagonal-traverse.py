class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        r, c = 0, 0
        direction = 1  # 1 for up-right, -1 for down-left

        while r < rows and c < cols:
            result.append(mat[r][c])
            new_row = r + (-1 if direction == 1 else 1)
            new_col = c + (1 if direction == 1 else -1)

            # Check for out of bounds and change direction accordingly
            if new_row < 0 or new_row == rows or new_col < 0 or new_col == cols:
                if direction == 1:
                    r += (c == cols - 1)  # Move down if on the last column
                    c += (c < cols - 1)   # Otherwise, move right
                else:
                    c += (r == rows - 1)  # Move right if on the last row
                    r += (r < rows - 1)   # Otherwise, move down
                direction *= -1  # Change direction
            else:
                r, c = new_row, new_col

        return result