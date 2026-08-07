# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, head = None, None
        c1, c2 = l1, l2
        total, carry = 0, 0 

        while c1 and c2:
            total = c1.val + c2.val + carry
            newNode = ListNode()

            # Set values
            if total < 10:
                newNode.val = total
                carry = 0
            else:
                newNode.val = total - 10
                carry = 1
            
            #  Link nodes
            if not head:
                prev, head = newNode, newNode
            else:
                prev.next = newNode
                prev = prev.next
            
            c1, c2 = c1.next, c2.next
        
        while c1:
            total = c1.val + carry
            newNode = ListNode()

            if total < 10:
                newNode.val = total
                carry = 0
            else:
                newNode.val = total - 10
                carry = 1
            prev.next = newNode
            prev = prev.next

            c1 = c1.next
        
        while c2:
            total = c2.val + carry
            newNode = ListNode()

            if total < 10:
                newNode.val = total
                carry = 0
            else:
                newNode.val = total - 10
                carry = 1
            
            prev.next = newNode
            prev = prev.next

            c2 = c2.next
        
        if carry > 0:
            newNode = ListNode()
            newNode.val = carry
            prev.next = newNode

        return head


