# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        stk = [[root, 0, 0]]
        max_val_stk = [root]

        while stk:
            node, leftProcessed, RightProcessed = stk[-1]
            if node is not max_val_stk[-1] and node.val >= max_val_stk[-1].val:
                res += 1
                max_val_stk.append(node)
            if not leftProcessed and node.left:
                stk[-1][1] = 1
                stk.append([node.left, 0, 0])
                continue
            if not RightProcessed and node.right:
                stk[-1][2] = 1
                stk.append([node.right, 0, 0])
                continue
            if max_val_stk and node is max_val_stk[-1]:
                max_val_stk.pop()

            stk.pop()

        return res


