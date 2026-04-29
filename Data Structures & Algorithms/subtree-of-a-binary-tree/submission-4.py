# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def dfs(node, subRoot):
            if not node:
                return False
            if sameTree(node, subRoot):
                return True
            return dfs(node.left, subRoot) or dfs(node.right, subRoot)
        


        def sameTree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if not subRoot and not root:
                return True
            if subRoot and root and subRoot.val == root.val:
                return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)
            return False
        
        return dfs(root, subRoot)     
        