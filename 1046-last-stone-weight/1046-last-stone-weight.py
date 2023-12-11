class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
#         stones = [-s for s in stones]
#         heapq.heapify(stones)
        
#         while len(stones) > 1:
#             first = heapq.heappop(stones)
#             second = heapq.heappop(stones)
#             if second > first:
#                 heapq.heappush(stones, first - second)
#         print(stones)
#         stones.append(0)
#         print(stones)
#         return abs(stones[0])
        heapq._heapify_max(stones)
        while len(stones) > 1:
            max_stone = heapq._heappop_max(stones)
            diff = max_stone - stones[0]
            if diff:
                heapq._heapreplace_max(stones, diff)
            else:
                heapq._heappop_max(stones)
        
        stones.append(0)
        return stones[0]