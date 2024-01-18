class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        # Function to count missing numbers up to index
        def missingCount(index):
            return nums[index] - nums[0] - index

        n = len(nums)
        if k > missingCount(n - 1):
            return nums[-1] + k - missingCount(n - 1)

        low, high = 0, n - 1
        while low < high:
            mid = (low + high) // 2
            if missingCount(mid) < k:
                low = mid + 1
            else:
                high = mid

        # low - 1 is the index where the kth missing number lies after
        return nums[low - 1] + k - missingCount(low - 1)