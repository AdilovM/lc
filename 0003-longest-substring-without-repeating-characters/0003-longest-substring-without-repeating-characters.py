class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited_chars = set()
        l = 0
        n = len(s)
        result = 0
        for r in range(n):
            while s[r] in visited_chars:
                visited_chars.remove(s[l])
                l += 1
            visited_chars.add(s[r])
            result = max(result, r - l + 1)
        return result