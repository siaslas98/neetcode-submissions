# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        res = False
        comp_res = True

        def compare(node1, node2):
            nonlocal comp_res

            if not node1 and not node2:
                return True
            if comp_res == False:
                return False

            if node1.val != node2.val:
                return False
            if (node1.left and not node2.left) or (node2.left and not node1.left):
                return False
            if (node1.right and not node2.right) or (node2.right and not node1.right):
                return False

            comp_res = compare(node1.left, node2.left) and compare(node1.right, node2.right)

            return comp_res

        def traverse(node):
            nonlocal res
            nonlocal comp_res

            if res == True:
                return

            if node.val == subRoot.val:
                res = compare(node, subRoot)
                comp_res = True
                
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        traverse(root)
        return res 