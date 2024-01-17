class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2

        # Step 1: Find the first decreasing element
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            # Step 2: Find the element to swap with
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the sublist from i+1 to end
        nums[i + 1:] = reversed(nums[i + 1:])

        # The function modifies the list in-place and does not return anything