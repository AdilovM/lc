class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0
        word_len, abbr_len = len(word), len(abbr)
        
        while i < word_len and j < abbr_len:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] == "0":
                return False
            elif abbr[j].isnumeric():
                k = j
                while k < abbr_len and abbr[k].isnumeric():
                    k += 1
                i += int(abbr[j:k])
                j = k
            else:
                return False
        return i == word_len and j == abbr_len