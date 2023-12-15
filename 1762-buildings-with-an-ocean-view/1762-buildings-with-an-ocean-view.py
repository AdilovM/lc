class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """
        traverse backwards and push each height into stack
        pop the stack if current height is taller than top of the stack and append output array
        """
        n = len(heights)
        answer = []
        max_height = -1
        
        for current in reversed(range(n)):
            if max_height < heights[current]:
                max_height = heights[current]
                answer.append(current)
                
        answer.reverse()
        return answer
                
                
            
        
        