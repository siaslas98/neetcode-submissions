# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = -1

        def search(root, k):
            nonlocal res

            if root.left:
                k = search(root.left, k)
            if res != -1:
                return res

            k -= 1
            if k == 0:
                res = root.val
                return res

            if root.right:
                k = search(root.right, k)
           
            if res != -1:
                return res

            return k
    

        search(root, k)
        return res
        
