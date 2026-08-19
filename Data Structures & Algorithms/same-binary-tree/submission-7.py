# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def traverse(node, s):
            if not node:
                return "/"
            if node.left:
                s += str(node.left.val)
                s = traverse(node.left, s)
            else:
                s += "-"
            if node.right:
                s += str(node.right.val)
                s = traverse(node.right, s)
            else:
                s += "-"
            
            s += str(node.val)

            return s
        
        s1 = traverse(p, "")
        s2 = traverse(q, "")

        return s1 + s2 == s2 + s1
