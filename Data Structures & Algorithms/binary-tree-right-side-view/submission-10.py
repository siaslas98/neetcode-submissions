# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
            
        res = []

        def dfs(node, target_level, level):
            nonlocal res

            if target_level == level:
                res.append(node.val)
                target_level += 1
            
            if node.right:
                target_level = dfs(node.right, target_level, level+1)
            
            if node.left:
                target_level = dfs(node.left, target_level, level+1)
            
            return target_level
        
        dfs(root, 1, 1)
        return res

            


        