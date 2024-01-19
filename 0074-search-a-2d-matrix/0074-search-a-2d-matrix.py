"""
if our target is within range of given row
we do another binary search and if target is not in that row, target is not in the given
matrix and we return False
""" 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # Start from the top-right corner of the matrix
        row, col = 0, len(matrix[0]) - 1

        # Iterate until we either find the target or exceed the bounds of the matrix
        while row < len(matrix) and col >= 0:
            # Compare the target with the current element
            if matrix[row][col] == target:
                return True  # Target found
            elif matrix[row][col] < target:
                row += 1  # Move down to the next row
            else:
                col -= 1  # Move left to the previous column

        return False  # Target not found




