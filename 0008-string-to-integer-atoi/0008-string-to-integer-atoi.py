class Solution:
    def myAtoi(self, s: str) -> int:
        i, n, sign = 0, len(s), 1
        maxInt, minInt = 2**31 - 1, -2**31

        # Skip leading whitespaces
        while i < n and s[i] == ' ':
            i += 1

        # Check for sign
        if i < n and (s[i] == '+' or s[i] == '-'):
            sign = 1 - 2 * (s[i] == '-')
            i += 1

        # Convert number
        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])
            # Check for overflow and underflow
            if num > (maxInt - digit) // 10:
                return maxInt if sign == 1 else minInt
            num = num * 10 + digit
            i += 1

        return sign * num