# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(pre, inord):

            if not pre:
                return None
            
            root = TreeNode(pre[0])

            idx = None
            for i, val in enumerate(inord):
                if val == pre[0]:
                    idx = i
                    break

            root.left = build(pre[1:idx+1], inord[:idx])
            root.right = build(pre[idx+1:], inord[idx+1:])
            return root
        
        return build(preorder, inorder)
            
