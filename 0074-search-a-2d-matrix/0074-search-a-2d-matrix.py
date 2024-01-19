"""
if our target is within range of given row
we do another binary search and if target is not in that row, target is not in the given
matrix and we return False
""" 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        upper, lower, target_row = 0, len(matrix) - 1, 0

        while upper <= lower:
            mid = (upper+lower)//2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                target_row = mid
                break
            elif target > matrix[mid][-1]:
                upper = mid + 1
            elif target < matrix[mid][0]:
                lower = mid - 1
            else:
                return False
        
        l, r = 0, len(matrix[target_row]) - 1
        while l<=r:
            mid = (l+r)//2
            if target < matrix[target_row][mid]:
                r = mid - 1
            elif target > matrix[target_row][mid]:
                l = mid + 1
            else:
                return True
        return False




