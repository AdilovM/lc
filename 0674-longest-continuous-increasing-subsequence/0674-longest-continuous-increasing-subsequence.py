class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count = 0
        result = 0
        for i in range(len(nums)):
            if i == 0:
                count += 1
            elif nums[i] > nums[i - 1]:
                count += 1
            else:
                result = max(result, count)
                count = 1
        return max(result, count)
                
        