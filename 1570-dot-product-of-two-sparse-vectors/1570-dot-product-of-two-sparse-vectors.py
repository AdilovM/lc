class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for i, num in enumerate(nums):
            if nums[i] != 0:
                self.non_zeros[i] = num
                

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:            
        output = 0
        for k in self.non_zeros:
            if k in vec.non_zeros:
                output += vec.non_zeros[k] * self.non_zeros[k]
        return output

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)