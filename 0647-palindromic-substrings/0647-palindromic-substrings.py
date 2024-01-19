class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0

        # Helper function to expand around the center and count palindromes
        def expandAroundCenter(left, right):
            nonlocal count
            while left >= 0 and right < N and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

        # Expand around each character and the gap between each pair of characters
        for i in range(N):
            # Odd length palindromes
            expandAroundCenter(i, i)
            # Even length palindromes
            expandAroundCenter(i, i + 1)

        return count