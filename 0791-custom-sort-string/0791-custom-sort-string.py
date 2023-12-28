class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        result = []
        
        for c in order:
            result.append(c * count[c])
            count[c] = 0
        
        for c in count:
            result.append(c * count[c])
        
        
        return "".join(result)