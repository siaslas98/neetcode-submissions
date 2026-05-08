# Definition for a binary tree node.
# class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (p and not q) or (not p and q):
            return False
        if not p and not q:
            return True

        res = True
        
        def traverse(p, q):
            nonlocal res

            if res == False:
                return

            if not p and not q:
                return

            if p.val != q.val:
                res = False
                return

            if (p.left and not q.left) or (q.left and not p.left):
                res = False
                return
            
            if (p.right and not q.right) or (q.right and not p.right):
                res = False
                return
            
            traverse(p.left, q.left)
            traverse(p.right, q.right)


        traverse(p, q)
        return res