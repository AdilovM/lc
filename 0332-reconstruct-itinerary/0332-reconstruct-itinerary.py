class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        # build a graph
        graph = defaultdict(list)
        for t in tickets:
            s, e = t
            graph[s].append(e)
        for k, v in graph.items():
            graph[k] = sorted(v)
        def dfs(airport):
            # post order dfs
            while graph[airport]:
                dfs(graph[airport].pop(0))
            res.append(airport)
        dfs("JFK")
        return res[::-1]