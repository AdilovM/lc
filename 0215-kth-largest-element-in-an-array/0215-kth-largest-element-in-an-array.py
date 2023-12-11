class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        curr = 0
        for _ in range(len(nums)):
            temp = heapq.heappop(nums)
            curr += 1
            if curr == k:
                return -temp
            