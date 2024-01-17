class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []  # Initialize an empty stack to store the digits

        for digit in num:  # Iterate through each digit in 'num'
            while k > 0 and stack and stack[-1] > digit:  # Check if the current digit is smaller than the stack's top
                stack.pop()  # Pop the top of the stack (remove a larger digit)
                k -= 1  # Decrease k as we have removed a digit
            stack.append(digit)  # Append the current digit to the stack

        # If k digits are not removed, remove from the end of the stack
        while k > 0:
            stack.pop()
            k -= 1

        # Convert stack to a string and remove leading zeros
        result = ''.join(stack).lstrip('0')

        return result if result else '0'