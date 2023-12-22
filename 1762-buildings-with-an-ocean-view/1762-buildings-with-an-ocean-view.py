class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        prev_max_height = -1
        output = []
        
        for current in range(len(heights) - 1, -1, -1):
            if prev_max_height < heights[current]:
                prev_max_height = heights[current]
                output.append(current)
                
        output.reverse()
        return output