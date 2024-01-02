class Solution:
    def calculate(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        curr_result = 0
        prev_result = 0
        final_result = 0
        sign = "+"
        
        
        for i in range(N):
            curr_char = s[i]
            
            if curr_char.isdigit():
                curr_result = curr_result * 10 + int(curr_char)
            
            if (not curr_char.isdigit() and not curr_char.isspace()) or i == N - 1:
                if sign in "+-":
                    final_result += prev_result
                    if sign == "+":
                        prev_result = curr_result
                    else:
                        prev_result = -curr_result
                elif sign == "*":
                    prev_result *= curr_result
                elif sign == "/":
                    prev_result = int(prev_result / curr_result)
                    
                sign = curr_char
                curr_result = 0
        
        final_result += prev_result
        return final_result