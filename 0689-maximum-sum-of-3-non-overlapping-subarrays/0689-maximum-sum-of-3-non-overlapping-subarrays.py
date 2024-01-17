class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Precompute sums of subarrays of size k
        n = len(nums)
        sums = [0] * (n - k + 1)
        current_sum = sum(nums[:k])
        sums[0] = current_sum
        for i in range(1, n - k + 1):
            current_sum += nums[i + k - 1] - nums[i - 1]
            sums[i] = current_sum

        # Dynamic programming to find the maximum sums
        left = [0] * len(sums)
        best = 0
        for i in range(len(sums)):
            if sums[i] > sums[best]:
                best = i
            left[i] = best

        right = [0] * len(sums)
        best = len(sums) - 1
        for i in range(len(sums) - 1, -1, -1):
            if sums[i] >= sums[best]:
                best = i
            right[i] = best

        # Find the maximum sum of three subarrays
        answer = [-1] * 3
        for j in range(k, len(sums) - k):
            if answer[0] == -1 or sums[left[j - k]] + sums[j] + sums[right[j + k]] > sums[answer[0]] + sums[answer[1]] + sums[answer[2]]:
                answer[0] = left[j - k]
                answer[1] = j
                answer[2] = right[j + k]

        return answer