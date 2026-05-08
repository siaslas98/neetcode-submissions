# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1, node2 = l1, l2

        while node1 and node2:
            s = node1.val + node2.val
            if s >= 10:
                node1.val = s % 10
                s //= 10
                if node1.next:
                    node1.next.val += s
                else:
                    if node2.next:
                        node2.next.val += s
                        node1.next = node2.next
                    else:
                        node1.next = ListNode(s)
                    node1 = node1.next
                    break
            else:
                node1.val = s
                if node1.next == None:
                    node1.next = node2.next
                    break
            
            node1 = node1.next
            node2 = node2.next

        while node1 and node1.val >= 10:
            s = node1.val // 10
            node1.val %= 10
            if node1.next:
                node1.next.val += s
            else:
                node1.next = ListNode(s)   
            node1 = node1.next
        

        return l1






