class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        create a list of 26 zeros.
        each index represents order of given chars. a is 0, b = 1 etc. index is calculated as ord(char) - ord('a') + 1
        each word is represented as list of zeros and ones. anagram words will be mapped to same list using defaultdict
        return values of defaultdict
        """
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[str(count)].append(s)
        return result.values()