class TicTacToe:

    def __init__(self, n: int):
        self.size = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        # Determine the player's mark value (1 for Player 1 and -1 for Player 2)
        player_val = 1 if player == 1 else -1

        # Update the counters for the row and column
        self.rows[row] += player_val
        self.cols[col] += player_val

        # Update the counter for the diagonal if necessary
        if row == col:
            self.diagonal += player_val

        # Update the counter for the anti-diagonal if necessary
        if row + col == self.size - 1:
            self.anti_diagonal += player_val

        # Check if this move wins the game
        if (abs(self.rows[row]) == self.size or
            abs(self.cols[col]) == self.size or
            abs(self.diagonal) == self.size or
            abs(self.anti_diagonal) == self.size):
            return player

        # Return 0 if no one wins
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)