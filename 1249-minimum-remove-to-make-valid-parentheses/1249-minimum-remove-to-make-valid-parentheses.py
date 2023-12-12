class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove = set()
        opening = []
        for idx, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                opening.append(idx)
            elif not opening:
                index_to_remove.add(idx)
            else:
                opening.pop()
        index_to_remove = index_to_remove.union(set(opening))
        print(index_to_remove)
        result = ""
        for idx, c in enumerate(s):
            if idx not in index_to_remove:
                result += c
        return result
        
        