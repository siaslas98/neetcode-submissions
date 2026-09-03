# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        tree = ""
        stk = [root]
        
        while stk:
            node = stk.pop()

            if not node:
                tree += "N,"
                continue

            stk.append(node.right)
            stk.append(node.left)
            tree += str(node.val) + ","

        return tree[:-1]

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        if data == "":
            return None
            
        values = data.split(",")
        n = len(values)

        root = TreeNode(int(values[0]))

        stk = [[root, 0]]
        
        for i in range(1, n):
            node, leftProcessed = stk[-1]
            curNode = None
            if values[i] != "N":
                curNode = TreeNode(int(values[i]))
            if leftProcessed:
                if values[i] == "N":
                    node.right = None
                else:
                    node.right = curNode
                stk.pop()
            
            else:
                if values[i] == "N":
                    node.left = None
                else:
                    node.left = curNode
                
                stk[-1][1] = 1
            
            if curNode:
                stk.append([curNode, 0])
        
        return root
            


