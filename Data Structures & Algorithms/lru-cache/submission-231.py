class Node:
    def __init__(self, key, val, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mapper = {}
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.mapper:
            node = self.mapper[key]

            if node is self.tail:
                return node.val
            if node is self.head and node.next:
                nextHead = node.next
                nextHead.prev = None
                self.tail.next = node
                node.prev = self.tail
                node.next = None
                self.tail = node
                self.head = nextHead
            else:
                prevNode = node.prev
                nextNode = node.next
                prevNode.next = nextNode
                nextNode.prev = prevNode
                self.tail.next = node
                node.prev = self.tail
                self.tail = node 
                node.next = None
            return node.val
        return -1 

    def put(self, key: int, value: int) -> None:
        if key in self.mapper:
            self.mapper[key].val = value
            self.get(key)
        else:
            node = Node(key=key, val=value)
            if len(self.mapper) + 1 > self.capacity:
                self.mapper.pop(self.head.key, None)
                if self.head.next:
                    nextHead = self.head.next
                    nextHead.prev = None
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node
                    self.head = nextHead
                else:
                    self.head, self.tail = node, node
            else:
                if not self.head:
                    self.head, self.tail = node, node
                else:
                    self.tail.next = node
                    node.prev = self.tail
                    self.tail = node

            self.mapper[key] = node

                


        
