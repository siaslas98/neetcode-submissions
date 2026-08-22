# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def search(node, left, right):
            if not node:
                return True
            
            
            if not (left < node.val < right):
                return False
            
            leftRes, rightRes = True, True
            
            if node.left:
                leftRes = search(node.left, left, node.val)
            if node.right:
                rightRes = search(node.right, node.val, right)
            
            return leftRes and rightRes
        
        return search(root, float('-inf'), float('inf'))
