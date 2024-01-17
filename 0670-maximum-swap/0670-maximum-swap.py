class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        # from right to left, store the position of the greatest value that is greater than self
        n = len(nums)
        pos = [None for _ in range(n)]
        pos[-1] = n - 1
        
        for i in reversed(range(n - 1)):  # O(N)
            if nums[i] <= nums[pos[i + 1]]:
                pos[i] = pos[i + 1]
            else:
                pos[i] = i

        for index, val in enumerate(nums):
            if nums[pos[index]] > val:
                right_index = pos[index]
                nums[index], nums[right_index] = nums[right_index], nums[index]
                break
        
        return int(''.join(nums))