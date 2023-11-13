class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_chars = {}
        t_chars = {}
        for c in s:
            s_chars[c] = s_chars.get(c, 0) + 1
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1
        
        for c in s_chars:
            if s_chars.get(c, 0) !=  t_chars.get(c, 0):
                return False
        return True