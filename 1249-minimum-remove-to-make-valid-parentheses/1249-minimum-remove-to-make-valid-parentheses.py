class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        opening_stack = []
        
        for idx, char in enumerate(s):
            if char not in "()":
                continue
            if char == "(":
                opening_stack.append(idx)
            elif not opening_stack:
                index_to_remove.add(idx)
            else:
                opening_stack.pop()
        
        index_to_remove = index_to_remove.union(set(opening_stack))
        
        res = ""
        for idx, char in enumerate(s):
            if idx not in index_to_remove:
                res += char
        return res