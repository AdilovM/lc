class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        to_add = 0
        for char in s:
            if char == "(":
                balance += 1
            elif char == ")":
                balance -= 1
                if balance < 0:
                    to_add += 1
                    balance = 0
        to_add += balance
        return to_add