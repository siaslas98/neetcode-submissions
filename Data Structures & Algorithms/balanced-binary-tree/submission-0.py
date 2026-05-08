# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        
        res = True
        
        def traverse(node):
            nonlocal res

            if res == False:
                return 0
                
            if not node.left and not node.right:
                return 1
            
            depth_left, depth_right = 0, 0

            if node.left:
                depth_left = traverse(node.left)
            if node.right:
                depth_right = traverse(node.right)
            if abs(depth_left-depth_right) > 1:
                res = False
                return 0
            
            return max(depth_left, depth_right) + 1
        

        traverse(root)
        return res
            

