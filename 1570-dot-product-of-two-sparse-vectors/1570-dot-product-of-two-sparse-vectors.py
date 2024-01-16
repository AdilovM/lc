class SparseVector:
    def __init__(self, nums: List[int]):
        # Assuming the constructor takes a list of numbers and converts it into a sparse representation
        self.nums = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        # Iterate over the shorter vector for efficiency
        if len(self.nums) < len(vec.nums):
            for idx, val in self.nums.items():
                if idx in vec.nums:
                    result += val * vec.nums[idx]
        else:
            for idx, val in vec.nums.items():
                if idx in self.nums:
                    result += val * self.nums[idx]

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)