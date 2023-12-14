class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums, 0, len(nums) - 1)
    def mergeSort(self, nums, start, end):
        if end - start + 1 <= 1:
            return nums
        mid = (start + end) // 2
        
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid + 1, end)
        
        self.merge(nums, start, mid, end)
        
        return nums
    
    def merge(self, nums, start, mid, end):
        left_nums = nums[start: mid + 1]
        right_nums = nums[mid + 1: end + 1]
        
        i, j, k = 0, 0, start
        
        while i < len(left_nums) and j < len(right_nums):
            if left_nums[i] <= right_nums[j]:
                nums[k] = left_nums[i]
                i += 1
            else:
                nums[k] = right_nums[j]
                j += 1
            k += 1
        
        while i < len(left_nums):
            nums[k] = left_nums[i]
            i += 1
            k += 1
        while j < len(right_nums):
            nums[k] = right_nums[j]
            j += 1
            k += 1
                