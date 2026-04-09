# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0 

        def depth(root: Optional[TreeNode]) -> int:
            nonlocal result 
            if not root:
                return 0
            
            right = depth(root.right)
            left = depth(root.left)

            result = max(result, right + left)

            return 1 + max(right,left)
        
        depth(root)
        return result
            

        
