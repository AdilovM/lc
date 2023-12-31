class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 1
        res = 0
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i- 1]:
                count += 1
            else:
                res = max(res, count)
                count = 1
        return max(res, count)