class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        zeroFirstRow, zeroFirstCol = False, False

        # Check if first row and first column need to be set to zero
        for i in range(m):
            if matrix[i][0] == 0:
                zeroFirstCol = True
                break

        for j in range(n):
            if matrix[0][j] == 0:
                zeroFirstRow = True
                break

        # Use first row and column as flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        # Set elements to zero based on flags
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Zero out first row and column if needed
        if zeroFirstCol:
            for i in range(m):
                matrix[i][0] = 0
        if zeroFirstRow:
            for j in range(n):
                matrix[0][j] = 0