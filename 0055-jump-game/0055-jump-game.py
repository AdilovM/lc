class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        max_reachable = 0  # Farthest reachable index

        for i in range(n):
            # If the current index is beyond the max reachable, you're stuck
            if i > max_reachable:
                return False

            # Update max reachable index
            max_reachable = max(max_reachable, i + nums[i])

            # If the max reachable is beyond or at the last index, you can reach the end
            if max_reachable >= n - 1:
                return True

        return False