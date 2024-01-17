class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Pointers for nums1, nums2, and the end position in nums1
        p1, p2, end = m - 1, n - 1, m + n - 1

        # Merge in reverse order
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[end] = nums1[p1]
                p1 -= 1
            else:
                nums1[end] = nums2[p2]
                p2 -= 1
            end -= 1

        # Fill nums1 with remaining nums2 elements, if any
        while p2 >= 0:
            nums1[end] = nums2[p2]
            p2 -= 1
            end -= 1
        # No need to check for remaining elements in nums1 since they are already in place

        # The function modifies nums1 in-place and does not return anything