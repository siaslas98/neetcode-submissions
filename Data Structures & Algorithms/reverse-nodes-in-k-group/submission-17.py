# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse_list(start, end):
            prev = ListNode()
            end.next = None
            cur = start

            while cur.next:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            cur.next = prev
            start.next = None
            
            return (cur, start)
        
        start, end = head, head
        prev_k, next_k = None, None
        count = 1

        while end and count != k:
            if end.next:
                end = end.next
                count += 1
                if count == k:
                    next_k = end.next
                    new_start, new_end = reverse_list(start, end)

                    if prev_k:
                        prev_k.next = new_start
                    else:
                        head = new_start

                    prev_k = new_end
                    new_end.next = next_k
                    start, end = next_k, next_k
                    count = 1
            else:
                return head
                
        return head

            