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
            node = stack.popleft()
            if not node[0]:
                continue
            if node[0].left:
                stack.append((node[0].left,node[1] + 1))
            if node[0].right:
                stack.append((node[0].right,node[1] + 1))
            result[node[1]].append(node[0].val)
        
        return list(result.values())