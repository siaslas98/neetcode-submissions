# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        A, B = [p], [q]
            
        while A and B:
            p, q = A.pop(), B.pop()

            if not p and not q:
                continue
            
            if not (p and q):
                return False

            if p.val != q.val:
                return False
            
            pLeft, pRight = p.left, p.right
            qLeft, qRight = q.left, q.right

            A.append(pLeft)
            B.append(qLeft)
            A.append(pRight)
            B.append(qRight)
        
        return True



