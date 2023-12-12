class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        def dfs(idx = 0, tmp = []):
            output.append(tmp)
            
            if idx == len(nums):
                return
            
            for i in range(idx, len(nums)):
                dfs(i + 1, tmp + [nums[i]])
                
        dfs()
        return output
                