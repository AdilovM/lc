# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def graph_builder(curr, parent):
            if curr and parent:
                graph[curr.val].append(parent.val)
                graph[parent.val].append(curr.val)
                
            if curr.left:
                graph_builder(curr.left, curr)
                
            if curr.right:
                graph_builder(curr.right, curr)
                
        graph_builder(root, None)
        
        output = []
        visited = set([target.val])
        
        def dfs(node_val, distance):
            if distance == k:
                output.append(node_val)
                return
            visited.add(node_val)
            for neighbor in graph[node_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
        dfs(target.val, 0)
        
        return output