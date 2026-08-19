# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        A, B = [p], [q]
        if not p and not q:
            return True
            
        while A and B:
            p, q = A.pop(), B.pop()

            if (not p and q) or (p and not q):
                return False

            if (p.left and not q.left) or (not p.left and q.left):
                return False
            if (p.right and not q.right) or (not p.right and q.right):
                return False
            if p.left and p.left.val != q.left.val:
                return False
            if p.right and p.right.val != q.right.val:
                return False
            if p.val != q.val:
                return False
            
            pLeft, pRight = p.left, p.right
            qLeft, qRight = q.left, q.right

            if pLeft:
                A.append(pLeft)
                B.append(qLeft)
            if p.right:
                A.append(pRight)
                B.append(qRight)
            
        if (A and not B) or (B and not A):
            return False
        
        return True



