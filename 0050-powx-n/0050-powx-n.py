class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case: Any number to the power of 0 is 1.
        if n == 0:
            return 1

        # If n is negative, work with its absolute value and invert the result.
        if n < 0:
            x = 1 / x
            n = -n

        # Recursively calculate the power.
        # If n is even, use the formula (x^n/2)^2.
        # If n is odd, use x * (x^n/2)^2.
        return self.myPow(x, n // 2) ** 2 if n % 2 == 0 else x * self.myPow(x, n // 2) ** 2