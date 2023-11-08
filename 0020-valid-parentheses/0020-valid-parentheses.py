class Solution:
    def isValid(self, s: str) -> bool:
        closing_parens = {
          ")" : "(",
          "}" : "{",
          "]" : "["
        }

        stack = []
        for c in s:
            if c not in closing_parens:
                stack.append(c)
            else:
                if len(stack) == 0 or closing_parens[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
    
        return not stack