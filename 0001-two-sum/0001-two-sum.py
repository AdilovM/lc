class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        for idx, num in enumerate(nums):
            if target - num in diff:
                return [diff[target-num], idx]
            else:
                diff[num] = idx
        return []
        