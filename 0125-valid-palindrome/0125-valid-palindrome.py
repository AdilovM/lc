class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            # move l
            while l < r and not self.is_alpha_num(s[l]):
                l += 1
            # move r
            while l < r and not self.is_alpha_num(s[r]):
                r -= 1
            
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
        
    def is_alpha_num(self, c):
        return (
            ord('a') <= ord(c) <= ord('z') or
            ord('A') <= ord(c) <= ord('Z') or
            ord('0') <= ord(c) <= ord('9')
        )