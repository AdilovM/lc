class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                num = board[row][col]
                if num != '.':
                    box_index = (row // 3) * 3 + col // 3

                    # Check if the number is already in the row, column or box
                    if num in rows[row] or num in cols[col] or num in boxes[box_index]:
                        return False

                    # Add the number to the row, column, and box set
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_index].add(num)

        return True