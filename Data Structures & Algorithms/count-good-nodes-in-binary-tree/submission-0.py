# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        max_val = root.val 

        def traverse(node, max_val):
            nonlocal count

            if node.val >= max_val:
                count += 1
            
            max_val = max(max_val, node.val)
            
            if node.left:
                traverse(node.left, max_val)
            if node.right:
                traverse(node.right, max_val)
            
        traverse(root, max_val)
        return count
