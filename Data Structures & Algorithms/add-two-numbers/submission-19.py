# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, head = None, None
        carry = 0
        c1, c2 = l1, l2

        while c1 or c2:
            if c1 and c2:
                total = c1.val + c2.val + carry
                c1 = c1.next
                c2 = c2.next
            elif c1:
                total = c1.val + carry
                c1 = c1.next
            else:
                total = c2.val + carry
                c2 = c2.next
            
            newNode = ListNode(total % 10)
            carry = total // 10

            if not head:
                prev, head = newNode, newNode
            else:
                prev.next = newNode
                prev = prev.next
        
        if carry == 1:
            prev.next = ListNode(1)
        
        return head