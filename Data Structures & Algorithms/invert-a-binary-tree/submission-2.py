# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        if not root.left and not root.right:
            return root

        rootLeft, rootRight = None, None
        
        if root.left:
            rootLeft = self.invertTree(root.left)
        if root.right:
            rootRight = self.invertTree(root.right)

        root.left, root.right = rootRight, rootLeft

        return root    