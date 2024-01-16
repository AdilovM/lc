class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        seen_digit = seen_dot = seen_e = False
        
        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True
            elif char == ".":
                if seen_e or seen_dot:
                    return False
                seen_dot = True
            elif char in ["e", "E"]:
                if not seen_digit or seen_e:
                    return False
                seen_e = True
                seen_digit = False
            elif char in ["+", "-"]:
                if i != 0 and s[i - 1] not in ["e", "E"]:
                    return False
            else:
                # invalid character
                return False
        return seen_digit