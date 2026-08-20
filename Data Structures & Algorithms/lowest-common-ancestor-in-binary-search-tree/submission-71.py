# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is p or root is q:
            return root
        resLeft, resRight = None, None
        if root.left:
            resLeft = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            resRight = self.lowestCommonAncestor(root.right, p, q)
        if resLeft and resRight:
            return root
        if resLeft:
            return resLeft
        if resRight:
            return resRight




        