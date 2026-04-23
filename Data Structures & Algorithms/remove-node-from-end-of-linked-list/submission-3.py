# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward = head

        while n - 1 > 0:
            forward = forward.next
            n -= 1
        
        remove = head
        dummy = ListNode()
        cur = dummy

        while forward.next:
            cur.next = remove
            cur = cur.next
            remove = remove.next
            forward = forward.next
        
        cur.next = remove.next
        return dummy.next



        