class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        idx_to_remove = set()
        opening = []
        for idx, char in enumerate(s):
            if char not in "()":
                continue
            elif char == "(":
                opening.append(idx)
            elif not opening:
                idx_to_remove.add(idx)
            else:
                opening.pop()
        idx_to_remove = idx_to_remove.union(set(opening))
        
        res = ""
        for idx, char in enumerate(s):
            if idx not in idx_to_remove:
                res += char
                
        return res