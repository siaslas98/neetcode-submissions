# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Use fast and slow pointer to traverse the list, we want to find the midpoint, then reverse right half
        slow, fast, prevSlow = head, head, None

        while fast and fast.next:
            prevSlow = slow
            fast = fast.next.next
            slow = slow.next

        if fast != None:
            prevSlow = slow
            slow = slow.next
    
        # Reverse the right half
        prev = None
        node = slow
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            if nxt == None:
                break
            node = nxt

        prevSlow.next = node
        
        left, right = head, prevSlow.next
        while left.next != right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            prevSlow.next = tmp2
            left = tmp1 
            right = tmp2
        

            





