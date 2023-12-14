class Solution:    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        temp_arr = [0] * len(nums)
        
        # Function to merge two sub-arrays in sorted order.
        def merge(left: int, mid: int, right: int):
            # Calculate the start and sizes of two halves.
            start1 = left
            start2 = mid + 1
            n1 = mid - left + 1
            n2 = right - mid

            # Copy elements of both halves into a temporary array.
            for i in range(n1):
                temp_arr[start1 + i] = nums[start1 + i]
            for i in range(n2):
                temp_arr[start2 + i] = nums[start2 + i]

            # Merge the sub-arrays 'in tempArray' back into the original array 'arr' in sorted order.
            i, j, k = 0, 0, left
            while i < n1 and j < n2:
                if temp_arr[start1 + i] <= temp_arr[start2 + j]:
                    nums[k] = temp_arr[start1 + i]
                    i += 1
                else:
                    nums[k] = temp_arr[start2 + j]
                    j += 1
                k += 1

            # Copy remaining elements
            while i < n1:
                nums[k] = temp_arr[start1 + i]
                i += 1
                k += 1
            while j < n2:
                nums[k] = temp_arr[start2 + j]
                j += 1
                k += 1

        # Recursive function to sort an array using merge sort
        def merge_sort(left: int, right: int):
            if left >= right:
                return
            mid = (left + right) // 2
            # Sort first and second halves recursively.
            merge_sort(left, mid)
            merge_sort(mid + 1, right)
            # Merge the sorted halves.
            merge(left, mid, right)
    
        merge_sort(0, len(nums) - 1)
        return nums[len(nums) - k]
#         def partition(left, right, pivot_index) -> int:
#             pivot = nums[pivot_index]
#             # Move pivot to the end
#             nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

#             # Move all larger elements to the left
#             store_index = left
#             for i in range(left, right):
#                 if nums[i] > pivot:
#                     nums[store_index], nums[i] = nums[i], nums[store_index]
#                     store_index += 1

#             # Move pivot to its final place
#             nums[right], nums[store_index] = nums[store_index], nums[right]
#             return store_index

#         def select(left, right, k_smallest) -> int:
#             if left == right:  # If the list contains only one element
#                 return nums[left]

#             # Select a random pivot_index
#             pivot_index = random.randint(left, right)

#             # Find the pivot position in a sorted list
#             pivot_index = partition(left, right, pivot_index)

#             # The pivot is in its final sorted position
#             if k_smallest == pivot_index:
#                 return nums[k_smallest]
#             elif k_smallest < pivot_index:
#                 return select(left, pivot_index - 1, k_smallest)
#             else:
#                 return select(pivot_index + 1, right, k_smallest)

#         return select(0, len(nums) - 1, k - 1)