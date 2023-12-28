# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = [root]
        while q:
            summ = 0
            level = 0
            temp = []
            while q:
                curr_node = q.pop()
                summ += curr_node.val
                level += 1
                if curr_node.left:
                    temp.append(curr_node.left)
                if curr_node.right:
                    temp.append(curr_node.right)
            q = temp
            res.append(summ * 1.0 / level)
        return res