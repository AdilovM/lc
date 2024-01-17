class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Here's a step-by-step approach:
        Sort Candidates (Optional): Sorting the candidates can sometimes make the algorithm more efficient, as it allows early termination in some cases.
        Backtracking Function:
        This function will take the current combination, the starting index for the next number, and the current sum.
        If the current sum equals the target, add the current combination to the result.
        If the current sum exceeds the target, terminate the current path.
        Iterate through the candidates starting from the current index:
        Add the candidate to the current combination.
        Recursively call the function with the updated combination, sum, and starting index (as candidates can be reused).
        Backtrack by removing the candidate from the current combination.
        Initialize and Invoke the Backtracking Function.
        """
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