class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearchLeft(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def binarySearchRight(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        start = binarySearchLeft(nums, target)
        end = binarySearchRight(nums, target)

        # Check if the target is not within the range of the array or doesn't exist
        if start > end:
            return [-1, -1]
        return [start, end]