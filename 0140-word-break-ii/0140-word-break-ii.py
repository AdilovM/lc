class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordSet:
                    rest_sentences = backtrack(end)
                    for sentence in rest_sentences:
                        full_sentence = s[start:end] + (" " + sentence if sentence else "")
                        sentences.append(full_sentence)

            memo[start] = sentences
            return sentences

        return backtrack(0)