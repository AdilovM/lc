class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: Any number to the power of 0 is 1
        if n == 0:
            return 1
        # Base case: 0 raised to any power is 0
        if x == 0:
            return 0

        # Handling negative n
        if n < 0:
            x = 1 / x
            n = -n

        # Exponentiation by squaring
        result = 1
        while n > 0:
            # If the n is odd, multiply the result with the x
            if n % 2:
                result *= x
            # Square the base
            x *= x
            # Halve the n
            n //= 2

        return result