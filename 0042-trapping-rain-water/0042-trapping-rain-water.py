class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        
        maxLeft = [0] * len(height)
        maxLeft[0] = height[0]
        maxRight = [0] * len(height)
        maxRight[-1] = height[-1]
        result = [0] * len(height)
        
        for i in range(1, len(height)):
            maxLeft[i] = max(maxLeft[i-1], height[i])
            
        print(maxLeft)
        for i in range(len(height) - 2, -1, -1):
            maxRight[i] = max(maxRight[i+1], height[i])
            
        print(maxRight)
        for i in range(len(height)):
            result[i] = min(maxLeft[i], maxRight[i])
        answer = 0
        
        for i in range(len(result)):
            answer += result[i] - height[i]
        
        
        return answer
                    
            
        
        