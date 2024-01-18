class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check if both words contain the same unique characters
        if set(word1) != set(word2):
            return False

        # Count the frequency of each character in both words
        from collections import Counter
        freq1 = Counter(word1)
        freq2 = Counter(word2)

        # Compare the frequency sets of both words
        return sorted(freq1.values()) == sorted(freq2.values())