class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next:
            return 
        s,f = head, head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next  
        
        second = s.next
        s.next = None

        prev = None 
        curr = second
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp 
        
        while head and prev:
            temp = head.next
            temp2 = prev.next
            head.next = prev 
            prev.next = temp
            prev = temp2
            head = temp
        return