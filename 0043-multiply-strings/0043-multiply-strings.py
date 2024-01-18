class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # If either of the number is 0, the result is 0
        if num1 == "0" or num2 == "0":
            return "0"

        # Initialize the result array with zeros
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        # Multiply each digit of num2 with each digit of num1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                # Add multiply result to the position (i + j + 1)
                p1, p2 = i + j, i + j + 1
                sum = mul + result[p2]

                # Update result array
                result[p1] += sum // 10
                result[p2] = sum % 10

        # Convert result to string, skipping leading zeros
        result_str = ''.join(map(str, result))
        return result_str.lstrip('0') 