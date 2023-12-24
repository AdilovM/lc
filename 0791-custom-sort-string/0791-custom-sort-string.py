class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        answer = []
        
        for c in order:
            answer.append(c * count[c])
            count[c] = 0
            
        for c in count:
            answer.append(c * count[c])
            
        return "".join(answer)