class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        sequence = defaultdict(list)
        for s in strings:
            key = []
            for i in range(1,len(s)):
                key.append((ord(s[i]) - ord(s[i - 1]))%26)
            sequence[tuple(key)].append(s)
        
        return [value for value in sequence.values()]
                