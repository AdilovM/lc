class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination, total):
            if total == target:
                result.append(combination.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(i, combination, total + candidates[i])
                combination.pop()

        result = []
        backtrack(0, [], 0)
        return result