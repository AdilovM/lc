class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count - not ordered
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # bucket = [[],[],[],[],[]] each index of bucket is count of number inside count dict    
        # [1,1,1] -> 3
        bucket = [[] for i in range(len(nums) + 1)]
        
        for num, freq in count.items():
            bucket[freq].append(num)
            
        
        result = []
        
        for i in range(len(bucket) -1, 0,-1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
                