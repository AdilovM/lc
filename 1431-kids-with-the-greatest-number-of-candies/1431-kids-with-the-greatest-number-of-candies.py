class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        local_max = max(candies)
        
        for idx, num in enumerate(candies):
            if num + extraCandies >= local_max:
                result[idx] = True
        return result