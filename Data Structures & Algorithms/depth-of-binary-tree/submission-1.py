#Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1

        def traverse(node, cur_depth):
            nonlocal depth
            
            depth = max(depth, cur_depth)
            if node.left:
                traverse(node.left, cur_depth+1)
            if node.right:
                traverse(node.right, cur_depth+1)
        
        traverse(root, 1)
        return depth
