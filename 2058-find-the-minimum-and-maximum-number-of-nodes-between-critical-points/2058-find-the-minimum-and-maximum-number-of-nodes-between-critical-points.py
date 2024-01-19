# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        # Traversing the list and identifying critical points
        prev, current = head, head.next
        position = 1
        critical_points = []

        while current and current.next:
            if (current.val > prev.val and current.val > current.next.val) or \
               (current.val < prev.val and current.val < current.next.val):
                critical_points.append(position)
            prev = current
            current = current.next
            position += 1

        # Calculating minimum and maximum distances
        if len(critical_points) < 2:
            return [-1, -1]

        min_distance = float('inf')
        max_distance = critical_points[-1] - critical_points[0]

        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i-1])

        return [min_distance, max_distance]
