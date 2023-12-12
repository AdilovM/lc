class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        # get freq of nums
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in counts.items():
            bucket[freq].append(num)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
            
        
        
        