"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pointers = {None: None}
        cur = head

        while cur:
            pointers[cur] = Node(cur.val)
            cur = cur.next
        
        for key in pointers:
            if key:
                node = pointers[key]
                ptr_next = key.next
                ptr_random = key.random
    
                node.next = pointers[ptr_next]
                node.random = pointers[ptr_random]
        
        return pointers[head]     