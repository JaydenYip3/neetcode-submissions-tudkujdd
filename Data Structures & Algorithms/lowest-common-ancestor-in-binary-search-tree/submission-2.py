# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pval, qval = p.val, q.val


        def dfs(node: TreeNode) -> TreeNode:
            if not node:
                return node 
            if node.val == pval or node.val == qval:
                return node
            if node.val > pval and node.val > qval:
                return dfs(node.left) 
            elif node.val < pval and node.val < qval:
                return dfs(node.right)
            else:
                return node
        
        return dfs(root)

        