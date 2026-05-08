# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def traverse(node, v, k):
            nonlocal res

            if res is not None:
                return res

            if node.left:
                v = traverse(node.left, v, k)

            v += 1
            if v == k:
                res = node.val
                return res

            if node.right:
                v = traverse(node.right, v, k)

            return v
        
        traverse(root, 0, k)
        return res
            




