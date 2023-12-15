class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        departure = set()
        
        for p in paths:
            departure.add(p[0])
        
        for p in paths:
            if p[1] not in departure:
                return p[1]