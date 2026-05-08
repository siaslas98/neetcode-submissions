class Node:
    def __init__(self, key, value, Prev=None, Next=None):
        self.key = key
        self.value = value
        self.Prev = Prev
        self.Next = Next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.mp = {}
        self.head, self.tail = None, None

    def get(self, key: int) -> int:
        if key in self.mp:
            # We want to place the node corresponding to this key at the end of the linked list
            node = self.mp[key]

            # Only one node
            if self.head == self.tail:
                return node.value

            # Already at tail, no need to move
            if node == self.tail:
                return node.value

            # We are at the head
            elif node == self.head:
                self.head = node.Next
                self.head.Prev = None

            # We are in the middle
            elif node.Prev and node.Next:
                node.Prev.Next = node.Next
                node.Next.Prev = node.Prev

            # Move to tail
            self.tail.Next = node
            node.Prev = self.tail
            node.Next = None
            self.tail = node

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        # We update the value for the node corresponding to key
        # Then we place this node at the end of our list
        if key in self.mp:
            node = self.mp[key]
            node.value = value

            # If node is the only one in the list, nothing to do
            if self.head == self.tail:
                return
            if node == self.tail:
                return
            if node == self.head:
                self.head = node.Next
                self.head.Prev = None
            elif node.Prev and node.Next:
                node.Prev.Next = node.Next
                node.Next.Prev = node.Prev

            # Move to tail
            self.tail.Next = node
            node.Prev = self.tail
            node.Next = None
            self.tail = node


        else:
            # We create the new node as if we want to append it to the end of the list
            newNode = Node(key, value)

            # Base case
            if not self.head and not self.tail:
                self.head, self.tail = newNode, newNode
                self.mp[key] = newNode
                return

            # If we exceed the capacity by putting one more node, delete from the head
            if len(self.mp) + 1 > self.capacity:
                if self.head == self.tail:
                    self.mp.pop(self.head.key)
                    self.head = self.tail = newNode
                    self.mp[key] = newNode
                    return
                else:
                    evicted = self.head
                    self.head = evicted.Next
                    self.head.Prev = None
                    self.mp.pop(evicted.key)

                    self.tail.Next = newNode
                    newNode.Prev = self.tail
                    self.tail = newNode
                    self.mp[key] = newNode
                    return

            else:
                self.tail.Next = newNode
                newNode.Prev = self.tail
                self.tail = newNode
                self.mp[key] = newNode
                return

            

                
              
            



          
            
         


                
