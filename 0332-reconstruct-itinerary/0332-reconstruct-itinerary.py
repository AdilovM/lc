class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def visit(airport):
            while graph[airport]:
                visit(graph[airport].pop())
            itinerary.append(airport)
    
        # Sort the tickets in reverse lexical order because we will pop from the end
        tickets.sort(key=lambda x: x[1], reverse=True)
        graph = defaultdict(list)
        for start, end in tickets:
            graph[start].append(end)

        itinerary = []
        visit('JFK')

        # The itinerary is constructed in reverse, so we need to reverse it back
        return itinerary[::-1]