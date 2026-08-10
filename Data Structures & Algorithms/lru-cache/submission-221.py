class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    def __init__(self, capacity: int):
       self.capacity = capacity
       self.h_map = {}
       self.head = None
       self.tail = None

    def get(self, key: int) -> int:
        node = self.h_map.get(key, -1)
        if type(node) is int:
            return -1
        if len(self.h_map) == 1 or node is self.tail:
            return node.val
        
        prevNode = node.prev
        nextNode = node.next
        
        if prevNode:
            prevNode.next = nextNode
            if nextNode:
                nextNode.prev = prevNode
        else:
            if nextNode:
                self.head = nextNode
                nextNode.prev = None
        if node is not self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            self.tail.next = None
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.h_map:
            node = self.h_map[key]
            node.val = value
            prevNode, nextNode = node.prev, node.next
            if node is self.tail:
                return

            if prevNode:
                prevNode.next = nextNode
                if nextNode:
                    nextNode.prev = prevNode
            else:
                if nextNode:
                    self.head = nextNode
                    nextNode.prev = None
            
            if self.tail is not node:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.tail.next = None
            
        else:
            # Creating a new node
            node = Node(key=key, val=value)

            if len(self.h_map) + 1 > self.capacity:
                # Remove the mapping
                self.h_map.pop(self.head.key, None)
                nextHead = self.head.next

                if nextHead:
                    self.head = nextHead
                    nextHead.prev = None
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:
                    self.head, self.tail = node, node
            else:
                if self.tail:

                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                else:
                    self.head, self.tail = node, node

            self.h_map[key] = node
            


            
            
                    



        
