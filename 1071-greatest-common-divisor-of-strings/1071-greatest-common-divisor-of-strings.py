"""
Time complexity: O(m+n)
We need to compare the two concatenations of length O(m+n), it takes O(m+n) time.
We calculate the GCD using binary Euclidean algorithm, it takes log(m⋅n) time.
To sum up, the overall time complexity is O(m+n).
Space complexity: O(m+n) We need to compare the two concatenations of length O(m+n).
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        max_len = gcd(len(str1), len(str2))
        return str1[:max_len]