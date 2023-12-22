class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        
        for x, y in points:
            min_heap.append((x**2 + y**2, [x,y]))
        
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            d, coord = heapq.heappop(min_heap)
            res.append(coord)
        return res