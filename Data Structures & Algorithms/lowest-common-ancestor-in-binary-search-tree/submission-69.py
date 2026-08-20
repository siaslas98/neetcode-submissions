# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(target, node, stk):
            stk.append(node)

            if node is target:
                return True
            
            if node.left:
                resLeft = search(target, node.left, stk)
                if resLeft:
                    return True
                
            if node.right:
                resRight = search(target, node.right, stk)
                if resRight:
                    return True

            stk.pop()
            return False
        

        A, B = [], []
        search(p, root, A)
        search(q, root, B)

        while len(A) < len(B):
            B.pop()
        while len(B) < len(A):
            A.pop()
            
        while True:
            nodeA, nodeB = A.pop(), B.pop()
            if nodeA is nodeB:
                return nodeA
        





