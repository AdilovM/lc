class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming bottom up
        # recursive: top down
        if not matrix or not matrix[0]:
            return 0
        H = len(matrix)
        W = len(matrix[0])
        # create a cache
        dp = [[0 for _ in range(W)] for _ in range(H)]
        answer = 0
        for row in range(H):
            for col in range(W):
                
                if matrix[row][col] == "1":
                    dp[row][col] = 1
                    if row > 0 and col > 0:
                        dp[row][col] += min(dp[row - 1][col], dp[row][col - 1], dp[row - 1][col -1])
                    answer = max(answer, dp[row][col])
        return answer * answer
        
    
        