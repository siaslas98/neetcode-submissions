# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True
            if not (p and q):
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right) and p.val == q.val

        leftResult, curResult, rightResult = False, False, False

        if root.left:
            leftResult = self.isSubtree(root.left, subRoot)
        
        if root.val == subRoot.val:
            curResult = sameTree(root, subRoot)
            if curResult:
                return curResult
        
        if root.right:
            rightResult = self.isSubtree(root.right, subRoot)
        
        return leftResult or curResult or rightResult
        




        
               

        
            
            
                


