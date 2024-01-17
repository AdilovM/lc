class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, cols = len(matrix), len(matrix[0])  # Get the dimensions of the matrix

        # Check each diagonal starting from the first column
        for row in range(rows):
            if not self.isDiagonalConsistent(matrix, row, 0):
                return False

        # Check each diagonal starting from the first row
        for col in range(1, cols):  # Start from 1 to avoid rechecking the first diagonal
            if not self.isDiagonalConsistent(matrix, 0, col):
                return False

        return True

    def isDiagonalConsistent(self, matrix, row, col):
        rows, cols = len(matrix), len(matrix[0])
        val = matrix[row][col]  # Value to compare in the diagonal

        while row < rows and col < cols:
            if matrix[row][col] != val:
                return False
            row += 1
            col += 1

        return True