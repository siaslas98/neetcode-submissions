# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiameter = 0

        def height(node):
            nonlocal maxDiameter

            if not node.left and not node.right:
                return 0

            maxLeft, maxRight = 0, 0 

            if node.left:
                maxLeft = height(node.left) + 1
            if node.right:
                maxRight = height(node.right) + 1
            
            maxDiameter = max(maxDiameter, maxLeft + maxRight, maxLeft, maxRight)

            return max(maxLeft, maxRight)

        height(root)
        return maxDiameter
            
        
        