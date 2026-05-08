
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
        mp = {}
        node, idx, new_nodes = head, 0, []

        while node:
            mp[node] = idx
            new_nodes.append(Node(node.val)) 
            node = node.next
            idx += 1

        rand_lst_indices = []
        node = head
        while node:
            rand_lst_indices.append(mp[node.random]) if node.random != None else rand_lst_indices.append(None)
            node = node.next
        
        for i in range(len(new_nodes)):
            new_nodes[i].next = new_nodes[i+1] if i < len(new_nodes)-1 else None
            new_nodes[i].random = new_nodes[rand_lst_indices[i]] if rand_lst_indices[i] != None else None
        
        
        return new_nodes[0]
        
        




        
        
    