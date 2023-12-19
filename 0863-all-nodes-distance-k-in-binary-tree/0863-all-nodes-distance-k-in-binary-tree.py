# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # convert tree into graph
        graph = defaultdict(list)
             
        def build_graph(node, parent):
            if node and parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)

            if node.left:
                build_graph(node.left, node)

            if node.right:
                build_graph(node.right, node)
                
        build_graph(root, None)    
        visited = set([target.val])
        answer = []
        
        
        def dfs(node_val, distance):
            if distance == k:
                answer.append(node_val)
                return
            for neighbor in graph[node_val]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    dfs(neighbor, distance + 1)
                    
        dfs(target.val, 0)
        return answer