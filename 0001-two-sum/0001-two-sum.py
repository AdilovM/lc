class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        
        for i in range(len(nums)):
            if target - nums[i] in diff:
                return [diff[target - nums[i]], i]
            else:
                diff[nums[i]] = i
                