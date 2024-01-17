class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle edge cases for overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        # Long division
        result = 0
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= temp << 1:
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        # Apply sign and return
        return sign * result