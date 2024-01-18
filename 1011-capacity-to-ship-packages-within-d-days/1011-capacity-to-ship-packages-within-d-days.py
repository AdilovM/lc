class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def canShip(capacity):
            total, day_count = 0, 1
            for weight in weights:
                total += weight
                if total > capacity:
                    day_count += 1
                    total = weight
            return day_count <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1

        return left