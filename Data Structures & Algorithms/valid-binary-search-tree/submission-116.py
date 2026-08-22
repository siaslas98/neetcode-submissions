# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True

        def search(root):
            if not root.left and not root.right:
                return (True, root.val, root.val)

            leftRes, rightRes = [True, float('inf'), float('-inf')], [True, float('inf'), float('-inf')]

            if root.left:
                leftRes = search(root.left)
            if root.right:
                rightRes = search(root.right)

            if not leftRes[0] or not rightRes[0]:
                return [False, -1, -1]

            return (leftRes[2] < root.val < rightRes[1], min(leftRes[1], rightRes[1], root.val), max(leftRes[2], rightRes[2], root.val))
        
        leftRes, rightRes = [True, float('inf'), float('-inf')], [True, float('inf'), float('-inf')]
        if root.left:
            leftRes = search(root.left)
        if root.right:
            rightRes = search(root.right)
        
        if not leftRes[0] or not rightRes[0]:
            return False

        return leftRes[2] < root.val < rightRes[1]
        
            
        