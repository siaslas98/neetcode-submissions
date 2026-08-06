
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        if not head.next:
            newNode = Node(head.val)
            newNode.next = None
            newNode.random = newNode if head.random else None
            return newNode

        # Create the copies
        old = head
        while old:
            newNode = Node(old.val)
            oldNext = old.next
            old.next = newNode
            newNode.next = oldNext
            old = oldNext
        
        # Setup random pointers
        old, new = head, head.next
        while True:
            if old.random:
                new.random = old.random.next
            
            old = new.next
            if not old:
                break
            new = old.next
        
        # Separte the old list from the new list
        old, new, newHead = head, head.next, head.next
        while True:
            if new.next:
                newNext = new.next
                new.next = newNext.next
                old.next = newNext
                new = new.next
                old = old.next
            else:
                old.next = None
                break
        
        return newHead
            

        



