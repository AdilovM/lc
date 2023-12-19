class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build and populate course : preqs graph
        graph = {course : [] for course in range(numCourses)}
        for course, preq in prerequisites:
            graph[course].append(preq)
            
        # dfs traversal. base cases: return False if there a cycle, return True if course has no preqs:
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if graph[course] == []:
                return True
            visited.add(course)
            for preq in graph[course]:
                if not dfs(preq):
                    return False    
            visited.remove(course)
            graph[course] = []
            return True
            
        # call dfs on each course
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
    
        