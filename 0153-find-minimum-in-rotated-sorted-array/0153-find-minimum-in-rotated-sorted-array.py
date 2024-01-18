class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return None

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:  # Pivot in the right half
                left = mid + 1
            else:  # Pivot in the left half or at mid
                right = mid

        return nums[left]