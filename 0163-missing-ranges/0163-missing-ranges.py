class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        nums = [lower - 1] + nums + [upper + 1]  # Adding boundaries

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1] + 1:  # Check if there is a gap
                res.append([nums[i - 1] + 1, nums[i] - 1])

        return res