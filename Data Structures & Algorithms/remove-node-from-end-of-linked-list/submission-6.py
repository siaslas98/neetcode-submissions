# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        node = head

        while node:
            length += 1
            node = node.next

        idx, node, prev = 0, head, None

        while node:
            if length - idx == n:
                if prev == None:
                    return node.next
                if node.next == None:
                    prev.next = None
                else:
                    prev.next = node.next
                    return head
                    
            idx += 1
            prev = node
            node = node.next
        return head

        

