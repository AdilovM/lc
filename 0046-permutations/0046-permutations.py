class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, end):
            # If we are at the end of the array, we have a complete permutation.
            if start == end:
                result.append(nums[:])
            for i in range(start, end):
                # Swap the current element with the start element.
                nums[start], nums[i] = nums[i], nums[start]
                # Recurse on the remaining elements.
                backtrack(start + 1, end)
                # Backtrack: undo the swap.
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0, len(nums))
        return result