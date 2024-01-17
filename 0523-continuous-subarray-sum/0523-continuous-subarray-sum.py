class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Special case handling
        if k == 0:
            return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))

        # Dictionary to store the earliest index of each modulo result
        modulo_dict = {0: -1}  # Initialize with 0: -1 to handle cases where the subarray starts from index 0
        prefixSum = 0

        for i, num in enumerate(nums):
            prefixSum += num
            modulo = prefixSum % k

            if modulo in modulo_dict:
                if i - modulo_dict[modulo] > 1:  # Check if subarray size is at least 2
                    return True
            else:
                modulo_dict[modulo] = i  # Store the earliest index

        return False