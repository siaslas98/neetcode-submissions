# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        n = len(inorder)
        h_map = {}
        for i, val in enumerate(inorder):
            h_map[val] = i

        def build(leftBound, rightBound, i):
            if leftBound > rightBound:
                return [None, i-1]
            root = TreeNode(preorder[i])
            if leftBound == rightBound:
                return [root, i]
            inorder_idx = h_map[preorder[i]]
            root.left, i = build(leftBound, inorder_idx-1, i+1)
            root.right, i = build(inorder_idx+1, rightBound, i+1)
            return [root, i]
        
        root, i = build(0, n-1, 0)  
        return root
                
            

