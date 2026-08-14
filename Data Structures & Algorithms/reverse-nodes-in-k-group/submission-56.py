# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse(self, head, tail):
        prev, cur = None, head

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()

        prevTail, nextHead, curHead, curTail = None, None, head, head
        length = 0

        while curTail:
            length += 1

            if length == k:
                nextHead = curTail.next
                curTail.next = None
                self.reverse(curHead, curTail)
                if prevTail:
                    prevTail.next = curTail
                else:
                    dummy.next = curTail
                prevTail = curHead
                curHead, curTail = nextHead, nextHead
                length = 0
            else:
                if curTail.next:
                    curTail = curTail.next
                else:
                    prevTail.next = curHead
                    break
            
        return dummy.next
