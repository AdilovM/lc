class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = int((l + r) // 2)
            if nums[m] < target:
                l = m + 1
            if nums[m] > target:
                r = m - 1
            if nums[m] == target:
                return m
        return -1
        