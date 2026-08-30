# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path_sum = float('-inf')

        def calculate(root):
            nonlocal max_path_sum
            
            leftPathSum, rightPathSum = float('-inf'), float('-inf')

            if root.left:
                leftPathSum = calculate(root.left)
            if root.right:
                rightPathSum = calculate(root.right)
            max_path_sum = max(max_path_sum, leftPathSum + root.val, rightPathSum + root.val, leftPathSum + rightPathSum + root.val, root.val)
            return max(leftPathSum + root.val, rightPathSum + root.val, root.val)

        calculate(root)
        return int(max_path_sum)

