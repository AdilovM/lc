class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        opening = []
        for idx, c in enumerate(s):
            if c not in "()":
                continue
            # if given char is "(" added to opening stack
            if c == "(":
                opening.append(idx)
            # if previous char wasnt "(" it was ")", add ")" to set
            elif not opening:
                index_to_remove.add(idx)
            # there is "(" in opening stack current ")", we pop opening stack
            else:
                opening.pop()
        # union index_to_remove set and opening set
        index_to_remove = index_to_remove.union(set(opening))
        
        result = ""
        for idx, c in enumerate(s):
            if idx not in index_to_remove:
                result += c
        return result
        
        