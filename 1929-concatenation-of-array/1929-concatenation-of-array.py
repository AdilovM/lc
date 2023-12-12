class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = [0] * 2 * len(nums)
        for idx in range(len(nums)):
            output[idx] = nums[idx]
            output[len(nums) + idx] = nums[idx]
        return output