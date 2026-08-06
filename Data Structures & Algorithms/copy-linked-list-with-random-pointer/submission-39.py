
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # pass 1:
        # create the copy of the original linked list, and set the next pointers correctly. Then do a map of nodeOriginal -> nodeNew
        # pass 2:
        # check the random pointer of the original list, map nodeNew.random to map[nodeOriginal.random]

        nodeMapper = {}
        newHead, prev, cur = None, None, head
        
        # Setup next pointer and node mappings
        while cur:
            newNode = Node(cur.val)
        
            if not newHead:
                newHead = newNode
            if prev:
                prev.next = newNode

            prev = newNode
            nodeMapper[cur] = newNode 
            cur = cur.next
        
        cur1, cur2 = head, newHead

        # Setup the random pointers
        while cur1:
            cur2.random = nodeMapper.get(cur1.random) 
            cur1, cur2 = cur1.next, cur2.next
        
        return newHead
        

            

            

            



