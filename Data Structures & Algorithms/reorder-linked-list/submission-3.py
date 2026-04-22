# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 

        half = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            half = half.next
        
        rev = None
        temp = half.next
        half.next = None
        half = temp

        while half:
            temp = half.next
            half.next = rev 
            rev = half
            half = temp
        
        cur = head
        while cur and rev:
            temp = cur.next
            temp2 = rev.next
            cur.next = rev
            rev.next = temp
            cur = temp
            rev = temp2       
         