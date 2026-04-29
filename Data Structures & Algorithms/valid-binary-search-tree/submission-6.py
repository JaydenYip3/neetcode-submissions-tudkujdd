# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], ul: int, ll: int) -> bool:
            if not node:
                return True
            if not (ll < node.val < ul):
                return False
              
            return dfs(node.left, node.val, ll) and dfs(node.right, ul, node.val)
              
        return dfs(root, float('inf'), float('-inf'))
            

        