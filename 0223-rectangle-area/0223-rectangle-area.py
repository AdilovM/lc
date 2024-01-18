class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # Calculate area of each rectangle
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)

        # Calculate overlap
        overlap_width = min(ax2, bx2) - max(ax1, bx1)
        overlap_height = min(ay2, by2) - max(ay1, by1)

        # Check if there is an overlap
        overlap_area = max(overlap_width, 0) * max(overlap_height, 0)

        # Total area is sum of areas of rectangles minus overlap
        return area1 + area2 - overlap_area