class Solution:    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        return nums[k-1]
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