# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        q = deque([root])
        children = []
        res = ""

        while q:
            node = q.popleft()
            if not node:
                res += "#,"
            else:
                res += str(node.val) + ","

            if node:
                children.append(node.left)
                children.append(node.right)

            if not q:
                res += "|,"
                q.extend(children)
                children.clear()
        
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # "1,|,2,3,|,#,#,4,5|,"
        
        if not data or data[0] == "#":
            return None

        def construct(parent_nodes, children):
            child_nodes = []
            for i in range(len(parent_nodes)):
                node = parent_nodes[i]

                if children[2*i] != "#":
                    node.left = TreeNode(int(children[2*i]))
                    child_nodes.append(node.left)
                if children[2*i+1] != "#":
                    node.right = TreeNode(int(children[2*i+1]))
                    child_nodes.append(node.right)
            return child_nodes


        segments = []
        i = 0
        while i < len(data):
            idx = data.find("|", i)
            if idx == -1:
                break
            segment = data[i:idx].strip(",")  # remove trailing comma
            segments.append(segment.split(","))
            
            i = idx + 1

        parent_nodes = [TreeNode(int(segments[0][0]))]
        root = parent_nodes[0]

        j = 1
        while j < len(segments):
            parent_nodes = construct(parent_nodes, segments[j])
            j+=1

        return root


    



