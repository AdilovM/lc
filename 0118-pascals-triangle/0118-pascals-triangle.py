class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row_num in range(numRows):
            # create row with row_num + 1 None elements
            row = [None for _ in range(row_num + 1)]
            # first and last elements are always 1
            row[0], row[-1] = 1, 1
            # fill in the rest values starting with second element bc first is always 1 till one before the last, last is always 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num -1][j]
            triangle.append(row)
            
        return triangle


      