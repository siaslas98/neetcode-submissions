# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        nxt = head.next
        prev = None
        head.next = prev

        while nxt:
            prev = head
            head = nxt
            nxt = nxt.next
            head.next = prev

        head.next = prev
        return head
        