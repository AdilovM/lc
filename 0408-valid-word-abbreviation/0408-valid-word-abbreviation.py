class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        return bool(re.match(re.sub('([1-9]\d*)', r'.{\1}', abbr) + '$', word))
            
            
                