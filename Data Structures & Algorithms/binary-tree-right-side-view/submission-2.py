# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = {}   

        def depth(root: Optional[TreeNode], height: int): 
            if not root:
                return 
            
            if height not in result:
                result[height] = []
            result[height].append(root.val)

            depth(root.left, height + 1)
            depth(root.right, height + 1)
 
        
        depth(root, 0)

        return [v[-1] for v in result.values()]



        