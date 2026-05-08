
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
        node = head
        idx = 0
        new_nodes = []

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
        
        for i in range(len(new_nodes)-1):
            new_nodes[i].next = new_nodes[i+1]
            new_nodes[i].random = new_nodes[rand_lst_indices[i]] if rand_lst_indices[i] != None else None
        
        if rand_lst_indices[len(new_nodes)-1] != None:
            new_nodes[len(new_nodes)-1].random = new_nodes[rand_lst_indices[len(new_nodes)-1]]
        else:
            new_nodes[len(new_nodes)-1].random = None
        
        return new_nodes[0]
        
        




        
        
    