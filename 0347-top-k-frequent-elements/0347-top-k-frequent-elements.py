class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count freq of each number
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # freq as an index
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in counts.items():
            bucket[freq].append(num)
        
        # traverse backwards and return k most freq nums
        res = []
        for idx in range(len(bucket) - 1, 0, -1):
            for n in bucket[idx]:
                res.append(n)
                if len(res) == k:
                    return res
                