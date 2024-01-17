class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0  # Initialize pointers
        intersections = []

        while i < len(firstList) and j < len(secondList):
            # Find the overlap between intervals
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])

            if start <= end:
                intersections.append([start, end])

            # Move the pointer that points to the interval with the smaller end time
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1

        return intersections