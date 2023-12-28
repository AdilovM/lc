class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 128
        for c in s:
            count[ord(c)] += 1
        for c in t:
            count[ord(c)] -= 1
            if count[ord(c)] < 0:
                return False
        return True