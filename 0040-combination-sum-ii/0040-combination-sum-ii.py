class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, combination, total):
            if total == target:
                result.append(combination.copy())
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                combination.append(candidates[i])
                backtrack(i + 1, combination, total + candidates[i])
                combination.pop()

        candidates.sort()
        result = []
        backtrack(0, [], 0)
        return result