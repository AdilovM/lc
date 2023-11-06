class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        maxLeft = [0] * len(height)
        maxLeft[0] = height[0]
        maxRight = [0] * len(height)
        maxRight[-1] = height[-1]
        result = 0
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])
            
        print(maxLeft)
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
            
        print(maxRight)
        for i in range(len(height)):
            result += min(maxLeft[i], maxRight[i]) - height[i]
        
        return result
                    
            
        
        