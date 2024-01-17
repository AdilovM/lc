class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []  # List to store the result digits
        carry = 0  # Initialize carry as 0

        # Start from the last digits of both strings
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            # Get the current digit for num1 and num2; if the index is out of range, use 0
            x1 = int(num1[i]) if i >= 0 else 0
            x2 = int(num2[j]) if j >= 0 else 0

            # Add the digits along with the carry
            value = x1 + x2 + carry
            carry = value // 10  # Update carry for next iteration
            value = value % 10  # Get the single digit

            # Prepend the digit to the result list
            result.append(str(value))

            # Move to the next digits
            i -= 1
            j -= 1

        # Reverse the result list and join to form the final result string
        return ''.join(reversed(result))