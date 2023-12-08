class Solution:
    def frequencySort(self, s: str) -> str:
        # count char freq
        counts = collections.Counter(s)
        max_heap = []
        heapq.heapify(max_heap)
        for char in counts:
            heapq.heappush(max_heap, (-counts[char], char))
        res = ""
        for i in range(len(max_heap)):
            f, c = heapq.heappop(max_heap)
            res += c * (-f)
            
        return res
        