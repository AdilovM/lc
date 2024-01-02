class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dp = [False] * (N + 1)
        dp[N] = True
        
        for i in range(N - 1, -1, -1):
            for w in wordDict:
                w_len = len(w)
                if (i + w_len) <= N and s[i : i + w_len] == w:
                    dp[i] = dp[i + w_len]
                if dp[i]:
                    break
        return dp[0]