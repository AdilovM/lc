class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
    
        def calculate(i, current_sum):
            if i == len(nums):
                return 1 if current_sum == target else 0
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]

            # Calculate the number of ways by considering both '+' and '-' for the current number
            add = calculate(i + 1, current_sum + nums[i])
            subtract = calculate(i + 1, current_sum - nums[i])

            memo[(i, current_sum)] = add + subtract
            return memo[(i, current_sum)]

        return calculate(0, 0)