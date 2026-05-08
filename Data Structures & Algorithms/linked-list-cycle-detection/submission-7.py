# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        idx = 0

        while node:
            node.val = idx
            if not node.next:
                return False
            if node.next.val < node.val:
                return True
            idx += 1
            node = node.next
            
        return False




