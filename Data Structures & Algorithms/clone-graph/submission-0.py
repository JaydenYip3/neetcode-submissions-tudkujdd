"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']: 
        if not node:
            return None 

        def dfs(node, mem={}):
            if node in mem:
                return mem[node]
            
            copy = Node(node.val)
            mem[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy   

        return dfs(node)


        
        