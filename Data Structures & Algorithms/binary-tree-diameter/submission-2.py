# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def traverse(node):
            nonlocal diameter

            if not node.left and not node.right:
                return 0
            
            left_depth, right_depth = 0, 0

            if node.left:
                left_depth = traverse(node.left) + 1
            if node.right:
                right_depth = traverse(node.right) + 1

            diameter = max(diameter, left_depth + right_depth)

            return max(left_depth, right_depth)
        
        traverse(root)
        return diameter