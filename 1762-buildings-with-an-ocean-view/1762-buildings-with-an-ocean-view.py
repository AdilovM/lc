class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        max_height = -1
        output = []
        
        for current in reversed(range(n)):
            if max_height < heights[current]:
                max_height = heights[current]
                output.append(current)
        output.reverse()
        return output