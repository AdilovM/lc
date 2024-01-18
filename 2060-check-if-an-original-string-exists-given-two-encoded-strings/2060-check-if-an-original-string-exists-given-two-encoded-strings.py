class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n = len(s1)  # Length of s1
        m = len(s2)  # Length of s2
        memo = dict()  # Memoization to store results of subproblems

        def helper(i, j, diff):
            # Base Case: If both strings are completely processed and diff is 0
            if i == n and j == m:
                return diff == 0

            # Return memoized result if available
            if (i, j, diff) in memo:
                return memo[(i, j, diff)]

            # Handle numeric characters in s1
            if i < n and s1[i].isdigit():
                num = 0
                k = i
                while k < n and s1[k].isdigit():
                    num = num * 10 + int(s1[k])  # Convert substring to number
                    k += 1
                    if helper(k, j, diff-num):  # Recur with updated diff
                        return True

            # Handle numeric characters in s2
            elif j < m and s2[j].isdigit():
                num = 0
                k = j
                while k < m and s2[k].isdigit():
                    num = num * 10 + int(s2[k])  # Convert substring to number
                    k += 1
                    if helper(i, k, diff+num):  # Recur with updated diff
                        return True

            # Handle matching characters
            elif diff == 0:
                if i < n and j < m and s1[i] == s2[j]:
                    return helper(i+1, j+1, diff)  # Recur for next characters

            # Adjust diff by moving in s2 if diff is negative
            elif diff < 0:
                if j < m:
                    return helper(i, j+1, diff+1)

            # Adjust diff by moving in s1 if diff is positive
            elif diff > 0:
                if i < n:
                    return helper(i+1, j, diff-1)

            # Memoize and return False if no condition is met
            memo[(i, j, diff)] = False
            return False

        return helper(0, 0, 0)  # Initial call to the helper function