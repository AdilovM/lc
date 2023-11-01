# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        def helper_dfs(node, current_path, current_sum):
            # if no more nodes, return back to recursive call
            if not node:
                return
            # add all nodes on same path
            current_path.append(node.val)
            
            # increment current_sum by node.val
            current_sum += node.val
            
            # if we are on leaves and if node vals/current_sum we traversed so far addes up to targetSum copy current_path into 
            # all_pathes bc that is one of root-to-leaf path that gives targetSum
            if not node.left and not node.right and current_sum == targetSum:
                all_pathes.append(list(current_path))
        
            # do the same for left and right children
            helper_dfs(node.left, current_path, current_sum)
            helper_dfs(node.right, current_path, current_sum)
            
            # since we've been adding all node vals into current_path and copied that current_path into all_pathes we need to reset/empty current_path
            current_path.pop()
            
        
        all_pathes = []
        helper_dfs(root, [], 0)
        return all_pathes
        