class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_non_zero_found_at = 0

        # Iterate over the array
        for cur in range(len(nums)):
            # If the current element is not zero,
            # swap it with the element at last_non_zero_found_at
            if nums[cur] != 0:
                nums[last_non_zero_found_at], nums[cur] = nums[cur], nums[last_non_zero_found_at]
                last_non_zero_found_at += 1