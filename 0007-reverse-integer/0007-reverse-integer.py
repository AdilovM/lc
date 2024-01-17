class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  # 32-bit integer maximum
        INT_MIN = -2**31     # 32-bit integer minimum

        sign = -1 if x < 0 else 1
        x = abs(x)
        reversed_x = 0

        while x != 0:
            digit = x % 10
            x //= 10

            # Check for overflow
            if reversed_x > INT_MAX // 10 or (reversed_x == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0

            reversed_x = reversed_x * 10 + digit

        return sign * reversed_x