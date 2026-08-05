# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next:
            return

        slow, fast = head, head
        length = 1

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            length += 2
        
        if fast.next:
            length += 1

        right = slow.next
        slow.next = None
        
        # reverse the right half
        prev, cur = None, right
        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        
        
        left, right = head, prev

        while left and right:
            leftNext = left.next
            rightNext = right.next

            left.next = right
            right.next = leftNext

            left = leftNext
            right = rightNext

        


            


     