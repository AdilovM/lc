class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))  # Convert the number to a list of its digits
        n = len(nums)  # Length of the number in terms of digits
        pos = [None for _ in range(n)]  # Initialize an array to store positions
        pos[-1] = n - 1  # The last digit is the greatest by default in its own position

        # Traverse the digits from right to left
        for i in reversed(range(n - 1)):  # O(N) - Iterate through the digits in reverse order
            # Compare each digit with the greatest digit found so far to its right
            if nums[i] <= nums[pos[i + 1]]:
                pos[i] = pos[i + 1]  # If the right digit is greater, update the position
            else:
                pos[i] = i  # Otherwise, the current digit is the greatest so far for its position

        # Traverse the digits from left to right to find the first digit that can be swapped
        for index, val in enumerate(nums):
            # If a greater digit is found on the right, perform the swap
            if nums[pos[index]] > val:
                right_index = pos[index]  # Get the index of the greater digit
                nums[index], nums[right_index] = nums[right_index], nums[index]  # Swap the digits
                break  # Break after the first swap as only one swap is needed

        return int(''.join(nums))  # Convert the list of digits back to an integer and return
