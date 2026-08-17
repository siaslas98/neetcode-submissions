# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        
        def height(node):
            nonlocal balanced

            if not node:
                return 0

            heightLeft, heightRight = 0, 0
        
            heightLeft = height(node.left)
            heightRight = height(node.right)

            if balanced == False:
                return

            if abs(heightLeft - heightRight) > 1:
                balanced = False

            return max(heightLeft, heightRight) + 1

        
        if not root:
            return True

        balanced = True

        height(root)
        return balanced

