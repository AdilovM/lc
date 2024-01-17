class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = digit_to_char[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path, and move on to the next digit
                backtrack(index + 1, path + [letter])

        combinations = []
        backtrack(0, [])
        return combinations