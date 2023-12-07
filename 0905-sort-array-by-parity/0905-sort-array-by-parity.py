class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        
        while l < r:
            if nums[l] % 2 > nums[r] % 2:
                t = nums[l]
                nums[l] = nums[r]
                nums[r] = t
            if nums[l] % 2 == 0:
                l += 1
            if nums[r] % 2 == 1:
                r -= 1
        return nums
                