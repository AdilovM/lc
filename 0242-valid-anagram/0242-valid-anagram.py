class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 128
        
        for char in s:
            count[ord(char)] += 1
        
        for char in t:
            count[ord(char)] -= 1
            if count[ord(char)] < 0:
                return False
            
        return True