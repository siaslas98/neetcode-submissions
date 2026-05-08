# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = [[root.val]]
        q = [root]
        children = []
        vals = []

        while q:
            for parent in q:
                if parent.left:
                    vals.append(parent.left.val)
                    children.append(parent.left)
                if parent.right:
                    vals.append(parent.right.val)
                    children.append(parent.right)
            
            if vals:
                res.append(vals[:])
            vals.clear()
            q = children[:]
            children.clear()
        
        return res
                
                


