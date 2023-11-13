class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        visited.add(nums[0])
        
        for i in range(1, len(nums)):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False