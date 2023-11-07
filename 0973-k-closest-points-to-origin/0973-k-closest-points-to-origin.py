class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = [(x**2 + y**2, i) for i, (x,y) in enumerate(points)]
        distances.sort()
        return [points[i] for (_, i) in distances[:k]]
            
            
            