# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True

        def traverse(node, left_child=None):
            nonlocal res
            if not node.left and not node.right:
                return (node.val, node.val)
            
            ret_max, ret_min = None, None
            left_max, right_max = None, None
            left_min, right_min = None, None

            if node.left:
                left_max, left_min = traverse(node.left, True)
                if res == False:
                    return (None, None)
                if left_max >= node.val:
                    res = False
                    return (None, None)

            if node.right:
                right_max, right_min = traverse(node.right, False)
                if res == False:
                    return (None, None)
                if right_min <= node.val:
                    res = False
                    return (None, None)

            if left_max and right_max:
                ret_max = max(left_max, right_max, node.val)
            elif left_max:
                ret_max = max(left_max, node.val)
            elif right_max:
                ret_max = max(right_max, node.val)


            if left_min and right_min:
                ret_min = min(left_min, right_min, node.val)
            elif left_min:
                ret_min = min(left_min, node.val)
            elif right_min:
                ret_min = min(right_min, node.val)
            

            return (ret_max, ret_min)
        
        traverse(root)
        return res
