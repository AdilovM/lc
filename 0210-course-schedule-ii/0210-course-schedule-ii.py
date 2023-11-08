class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {i:[] for i in range(numCourses)}
        
        for c, p in prerequisites:
            preqMap[c].append(p)
        visited = set()
        result = []
        currentPath = set()
        def helper_dfs(crs):
            if crs in currentPath:
                return False
            if crs in visited:
                return True
            currentPath.add(crs)
            visited.add(crs)
            
            for pre in preqMap[crs]:
                if not helper_dfs(pre): return False
            
            currentPath.remove(crs)
            result.append(crs)
            preqMap[crs] = []
            
            return True
        
        for crs in range(numCourses):
            if not helper_dfs(crs): return []
        return result
                