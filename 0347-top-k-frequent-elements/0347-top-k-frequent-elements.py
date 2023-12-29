class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i, num in enumerate(nums):
            dic[num] = dic.get(num,0) + 1
        
        heap=[]
        for item in dic.items():
            key, value = item
            heapq.heappush(heap, (value,key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for value, key in heap:
            res.append(key)
        return res
                