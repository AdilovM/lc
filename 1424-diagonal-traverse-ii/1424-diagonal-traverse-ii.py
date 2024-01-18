class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diagonal_dict = {}
    
        # Group elements into diagonals
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i + j not in diagonal_dict:
                    diagonal_dict[i + j] = []
                diagonal_dict[i + j].append(nums[i][j])

        result = []
        # Flatten the diagonals into the result list
        for diagonal in sorted(diagonal_dict.keys()):
            result.extend(reversed(diagonal_dict[diagonal]))

        return result