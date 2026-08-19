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
        if (not p and q) or (p and not q):
            return False

        while A and B:
            if (p.left and not q.left) or (not p.left and q.left):
                return False
            if (p.right and not q.right) or (not p.right and q.right):
                return False
            if p.left and p.left.val != q.left.val:
                return False
            if p.right and p.right.val != q.right.val:
                return False
            
            p, q = A.pop(), B.pop()
            if p.val != q.val:
                return False

            if p.left:
                p, q = p.left, q.left
                A.append(p)
                B.append(q)
            if p.right:
                p, q = p.right, q.right
                A.append(p)
                B.append(q)
        
        if A or B:
            return False
        
        return True


