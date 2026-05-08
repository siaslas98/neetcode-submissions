# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        # Initialize final list with dummy node
        dummy_head = ListNode()
        tail = dummy_head

        while True:
            min_node_idx = None

            # Find the node with the smallest value across lists
            for i, lst in enumerate(lists):
                if not lst:
                    continue
                if min_node_idx is None:
                    min_node_idx = i
                    continue
                if lst.val < lists[min_node_idx].val:
                    min_node_idx = i

            if min_node_idx is None:
                break

            tail.next = lists[min_node_idx]
            lists[min_node_idx] = lists[min_node_idx].next
            tail = tail.next
            
        return dummy_head.next
