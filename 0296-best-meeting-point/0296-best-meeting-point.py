class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def minDistance1D(points: List[int]) -> int:
        # Find the median and calculate the distance to it
            points.sort()
            median = points[len(points) // 2]
            return sum(abs(p - median) for p in points)

        rows, cols = [], []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    rows.append(r)
                    cols.append(c)

        # Calculate total minimum distance
        return minDistance1D(rows) + minDistance1D(cols)