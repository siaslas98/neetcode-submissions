# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stk = [{"node": root,
                "leftProcessed": False,
                "rightProcessed": False,
                "leftHeight": -1,
                "rightHeight": -1,
                "height": 0
              }]

        while stk:
            cur = stk[-1]

            if cur["leftProcessed"] and cur["rightProcessed"]:
                cur = stk.pop()
                if abs(cur["leftHeight"] - cur["rightHeight"]) > 1:
                    return False
                cur["height"] = max(cur["leftHeight"], cur["rightHeight"]) + 1
                if stk:
                    parent = stk[-1]
                    if cur["node"] is parent["node"].left:
                        parent["leftProcessed"] = True
                        parent["leftHeight"] = cur["height"]
                    else:
                        parent["rightProcessed"] = True
                        parent["rightHeight"] = cur["height"]
                    
            if not cur["leftProcessed"]:
                if cur["node"].left:
                    stk.append({
                                "node": cur["node"].left,
                                "leftProcessed": False,
                                "rightProcessed": False,
                                "leftHeight": -1,
                                "rightHeight": -1,
                                "height": 0
                    })
                    continue
                else:
                    cur["leftProcessed"] = True
            
            if not cur["rightProcessed"]:
                if cur["node"].right:
                    stk.append({
                                "node": cur["node"].right,
                                "leftProcessed": False,
                                "rightProcessed": False,
                                "leftHeight": -1,
                                "rightHeight": -1,
                                "height": 0
                    })
                    continue
                else:
                    cur["rightProcessed"] = True
        
        return True 




            


            
            
            



