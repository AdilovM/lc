class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # Initialize pointers for the sliding window
        left = right = 0
        # To count the number of zeros in the current window
        zero_count = 0
        # To keep track of the maximum length of a window with at most k zeros
        max_length = 0

        # Iterate through the array with the right pointer
        while right < len(nums):
            # If the current element is 0, increment the zero_count
            if nums[right] == 0:
                zero_count += 1

            # If the number of zeros exceeds k, shrink the window from the left
            while zero_count > k:
                # If the leftmost element is zero, decrement the zero_count
                if nums[left] == 0:
                    zero_count -= 1
                # Move the left pointer to the right to shrink the window
                left += 1

            # Update the max_length of the window found so far
            max_length = max(max_length, right - left + 1)
            # Expand the window by moving the right pointer
            right += 1

        # Return the maximum length of a window with at most k zeros
        return max_length