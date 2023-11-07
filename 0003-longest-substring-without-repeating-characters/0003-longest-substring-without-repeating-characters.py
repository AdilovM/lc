class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        N = len(s)
        l, r = 0 , 0
        max_substring_length = 0
        
        while r < N:
            if s[r] not in char_set:
                char_set.add(s[r])
                r += 1
                max_substring_length = max(max_substring_length, r - l)
            else:
                char_set.remove(s[l])
                l+= 1
        return max_substring_length
                