class Solution:
    def isValid(self, s: str) -> bool:
        closed_parens = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        stack = []
        
        for c in s:
            if c not in closed_parens:
                stack.append(c)
            else:
                if len(stack) == 0 or closed_parens[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        return not stack
            
                