class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        # populate list with set of distance, x, y
        for x, y in points:
            distance = (x ** 2 + y ** 2)
            min_heap.append((distance, x, y))
            
        # heapify the list
        heapq.heapify(min_heap)
        res = []
        for i in range(k):
            distance, x, y = heapq.heappop(min_heap)
            res.append((x, y))
        return res