class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            hours_spent = sum((pile - 1) // mid + 1 for pile in piles)  # Ceiling division

            if hours_spent <= h:  # If this speed is feasible
                right = mid
            else:  # If this speed is not feasible
                left = mid + 1

        return left