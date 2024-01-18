class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)
        memo = dict()

        def helper(i, j, diff):
            if i == n and j == m:
                return diff == 0
            if (i, j, diff) in memo:
                return memo[(i, j, diff)]

            if i < n and s1[i].isdigit():
                num = 0
                k = i
                while k < n and s1[k].isdigit():
                    num = num * 10 + int(s1[k])
                    k += 1
                    if helper(k, j, diff-num):
                        return True
            elif j < m and s2[j].isdigit():
                num = 0
                k = j
                while k < m and s2[k].isdigit():
                    num = num * 10 + int(s2[k])
                    k += 1
                    if helper(i, k, diff+num):
                        return True
            elif diff == 0:
                if i < n and j < m and s1[i] == s2[j]:
                    return helper(i+1, j+1, diff)
            elif diff < 0:
                if j < m:
                    return helper(i, j+1, diff+1)
            elif diff > 0:
                if i < n:
                    return helper(i+1, j, diff-1)

            memo[(i, j, diff)] = False
            return False

        return helper(0, 0, 0)
