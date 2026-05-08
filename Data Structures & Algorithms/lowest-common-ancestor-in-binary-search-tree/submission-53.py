# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        find_p = True
        a1, a2 = [], []

        def find(node, target):
            nonlocal a1, a2, find_p

            if node.val == target.val:
                (a1 if find_p else a2).append(node)
                return True

            if (node.left and find(node.left, target)) or (node.right and find(node.right, target)):
                (a1 if find_p else a2).append(node)
                return True

            return False
        
        find(root, p)
        find_p = False
        find(root, q)
        
        i, j = len(a1)-1, len(a2)-1
        lca = None

        while i >= 0 and j >= 0:
            if a1[i] == a2[j]:
                lca = a1[i]
            i-=1
            j-=1
            
        return lca

        

        
            

