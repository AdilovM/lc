class Solution:
    def calculate(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0

        currentNumber = 0
        lastNumber = 0
        result = 0
        sign = '+'

        for i in range(length):
            currentChar = s[i]
            if currentChar.isdigit():
                currentNumber = (currentNumber * 10) + int(currentChar)
            
            if (not currentChar.isdigit() and not currentChar.isspace()) or i == length - 1:
                if sign == '+' or sign == '-':
                    result += lastNumber
                    lastNumber = currentNumber if sign == '+' else -currentNumber
                elif sign == '*':
                    lastNumber *= currentNumber
                elif sign == '/':
                    lastNumber = int(lastNumber / currentNumber)  # Integer division

                sign = currentChar
                currentNumber = 0
        
        result += lastNumber
        return result
