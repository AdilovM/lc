class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        l, res, N = 0, 0, len(colors)
        for r in range(1, N):
            if colors[l] == colors[r]:
                if neededTime[l] < neededTime[r]:
                    res += neededTime[l]
                    l = r
                else:
                    res += neededTime[r]
            else:
                l = r
        return res