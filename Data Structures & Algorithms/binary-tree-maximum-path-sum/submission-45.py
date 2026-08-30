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
            if not root:
                return 0
            left = max(calculate(root.left), 0)
            right = max(calculate(root.right), 0)

            max_path_sum = max(max_path_sum, root.val + left + right)
            return root.val + max(left, right)

        calculate(root)
        return int(max_path_sum)