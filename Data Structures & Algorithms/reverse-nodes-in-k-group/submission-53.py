# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse(self, headNode, tailNode):
        prev, cur = None, headNode

        while cur:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            if nextNode is tailNode.next:
                break
            cur = nextNode

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        prev, cur = None, head
        length = 1
        pairs = []

        pairHead, pairTail = head, None

        while True:
            while length < k:
                if cur.next:
                    cur = cur.next
                    length += 1
                else:
                    break

            if length < k:
                pairs.append((None, pairHead))
                break
            else:   
                pairs.append((pairHead, cur))

            pairHead = cur.next
            cur = pairHead

            if not pairHead:
                break

            length = 1
        
        for pair in pairs:
            if pair[0] is not None:
                pair[1].next = None
                self.reverse(pair[0], pair[1])
        
        for i in range(len(pairs)-1):
            tailLeft = pairs[i][0]
            headRight = pairs[i+1][1]
            tailLeft.next = headRight

        return pairs[0][1]


        

        

