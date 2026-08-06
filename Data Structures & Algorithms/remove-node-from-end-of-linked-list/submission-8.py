# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            head = None
            return head
        
        L = 0 
        cur = head

        while cur:
            L += 1
            cur = cur.next
        
        prev, cur = None, head
        forwardIdx = 1

        while cur:
            reverseIdx = L - forwardIdx + 1
            if reverseIdx == n:
                if prev:
                    prev.next = cur.next
                    cur = None
                else:
                    cur = cur.next
                    head = cur
                
                return head

            prev = cur
            cur = cur.next
            forwardIdx += 1
        
        

