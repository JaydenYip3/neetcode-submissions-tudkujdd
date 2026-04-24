# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while True:
            mini = float('inf') 
            smallest = None
            nulls = 0
            index = -1
            for i, head in enumerate(lists):
                if not head: 
                    nulls += 1
                    continue
                if head.val < mini:
                    index = i
                    mini = head.val
            if nulls == len(lists):
                break
            smallest = lists[index]
            lists[index] = lists[index].next
            cur.next = smallest
            cur = cur.next
        
        return dummy.next          