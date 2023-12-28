# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return None
        q = deque([root])
        result = []
        while q:
            size = len(q)
            summ = 0
            for i in range(size):
                node = q.popleft()
                summ += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(summ  * 1.0 / size)
        return result