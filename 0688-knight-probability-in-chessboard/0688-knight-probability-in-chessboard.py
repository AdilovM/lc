class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Define the possible moves of a knight
        moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]

        # Memoization table
        memo = {}

        def dp(k, r, c):
            # Check if out of the board
            if r < 0 or c < 0 or r >= n or c >= n:
                return 0
            # If no more moves, the knight is on the board
            if k == 0:
                return 1
            # Check memo table
            if (k, r, c) in memo:
                return memo[(k, r, c)]

            # Calculate the probability
            prob = 0
            for dr, dc in moves:
                prob += dp(k - 1, r + dr, c + dc) / 8

            # Save in memo table
            memo[(k, r, c)] = prob
            return prob
        # Initial call to the recursive function
        return dp(k, row, column)