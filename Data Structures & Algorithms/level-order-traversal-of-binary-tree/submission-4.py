# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        stack = collections.deque([(root, 0)]) 
        result = defaultdict(list) 

        while stack:
            node, depth = stack.popleft()
            if not node:
                continue
            if node.left:
                stack.append((node.left ,depth + 1))
            if node.right:
                stack.append((node.right,depth + 1))
            result[depth].append(node.val)
        
        return list(result.values())