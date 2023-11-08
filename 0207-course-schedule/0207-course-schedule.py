class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        numCourses = 5
        prerequisites = [[0,1],[0,2],[1,3],[1,4],[3,4]]
        preqMap
        course | preq
        0       | [1,2]
        1       | [3,4]
        2       | []  
        3       | [4]
        4       | []
        """
        preqMap = {i:[] for i in range(numCourses)}
        
        for c, p in prerequisites:
            preqMap[c].append(p)
        visited = set()
        def helper_dfs(crs):
            if crs in visited:
                return False
            if preqMap[crs] == []:
                return True
            visited.add(crs)
            
            for pre in preqMap[crs]:
                if not helper_dfs(pre): return False
            visited.remove(crs)
            preqMap[crs] = []
            return True
        for crs in range(numCourses):
            if not helper_dfs(crs): return False
        return True
                