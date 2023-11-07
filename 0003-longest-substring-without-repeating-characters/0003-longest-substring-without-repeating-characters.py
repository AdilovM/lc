class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        N = len(s)
        l = 0
        max_substring_length = 0
        
        for r in range(N):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_substring_length = max(max_substring_length, r - l + 1)
        return max_substring_length