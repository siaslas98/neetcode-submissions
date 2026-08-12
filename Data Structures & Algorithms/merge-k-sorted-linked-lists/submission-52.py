# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy

        heap = [(node.val, index, node)
                for index, node in enumerate(lists)
                if node
        ]

        heapq.heapify(heap)

        while heap:
            val, index, nextNode = heapq.heappop(heap)
            cur.next = nextNode
            nextHead = nextNode.next
            if nextHead:
                heapq.heappush(heap, (nextHead.val, index, nextHead))
            cur = cur.next
        
        return dummy.next