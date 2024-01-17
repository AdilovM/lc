class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        To find the first missing positive integer in an unsorted array, we can use an approach that places each number in its "correct" position if                   possible. For instance, the number 1 should be placed at index 0, 2 at index 1, and so on. 
        This is known as the cyclic sort method. 
        The idea is to iterate  through the array and for each number, try to place it in its correct position.
        Here's a step-by-step approach:
        Iterate Over the Array:
        For each number, if it is in the range [1, len(nums)] and not already in its correct position, swap it with the number at its correct position.
        Find the Missing Positive:

        After the above step, iterate through the array again.
        The first position where the number is not equal to its index + 1 is the first missing positive.
        Handle Edge Cases:
        If all numbers from 1 to len(nums) are present, then the answer is len(nums) + 1.

        """
        n = len(nums)
    
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1