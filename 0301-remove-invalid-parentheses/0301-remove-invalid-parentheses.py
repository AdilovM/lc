class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            balance = 0
            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    if balance == 0:
                        return False
                    balance -= 1
            return balance == 0

        def backtrack(start, left_count, right_count, left_rem, right_rem, path):
            if left_rem < 0 or right_rem < 0:
                return
            if start == len(s):
                if left_rem == 0 and right_rem == 0 and isValid(path):
                    result.add(path)
                return

            if s[start] == '(':
                backtrack(start + 1, left_count, right_count, left_rem - 1, right_rem, path)  # Remove it
                backtrack(start + 1, left_count + 1, right_count, left_rem, right_rem, path + s[start])  # Keep it
            elif s[start] == ')':
                backtrack(start + 1, left_count, right_count, left_rem, right_rem - 1, path)  # Remove it
                backtrack(start + 1, left_count, right_count + 1, left_rem, right_rem, path + s[start])  # Keep it
            else:
                backtrack(start + 1, left_count, right_count, left_rem, right_rem, path + s[start])  # Non-parenthesis characters

        # Count the number of misplaced left and right parentheses
        left_rem, right_rem = 0, 0
        for char in s:
            if char == '(':
                left_rem += 1
            elif char == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()
        backtrack(0, 0, 0, left_rem, right_rem, "")
        return list(result)