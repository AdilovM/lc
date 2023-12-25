class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build graph
        graph = {i : [] for i in range(numCourses)}
        visited = set()
        # populate the graph
        for crs, preq in prerequisites:
            graph[crs].append(preq)
        
        def dfs(crs):
            if graph[crs] == []:
                return True
            if crs in visited:
                return False
            visited.add(crs)
            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            
            visited.remove(crs)
            graph[crs] = []
            return True
            
        
        for crs in graph:
            if not dfs(crs):
                return False
        return True
            
                
                