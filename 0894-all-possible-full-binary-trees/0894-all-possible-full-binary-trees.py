# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # Memoization to store previously computed results
        if n % 2 == 0:  # No full binary trees are possible with even number of nodes
            return []
        if n == 1:  # Base case: a single node
            return [TreeNode(0)]

        if n in memo:
            return memo[n]

        result = []
        for left_nodes in range(1, n, 2):  # Iterate over odd numbers
            right_nodes = n - 1 - left_nodes
            for left_tree in self.allPossibleFBT(left_nodes):
                for right_tree in self.allPossibleFBT(right_nodes):
                    root = TreeNode(0)  # Each tree has 0 as its value (as per problem statement)
                    root.left = left_tree
                    root.right = right_tree
                    result.append(root)
        
        memo[n] = result  # Save the computed result
        return result

# Global dictionary for memoization
memo = {}