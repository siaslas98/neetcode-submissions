class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        mp = {"(":")",
              "{":"}",
              "[":"]"}

        for c in s:
            if c in mp:
                stk.append(c)
            elif not stk:
                return False
            elif mp[stk[-1]] != c:
                return False
            else:
                stk.pop()

        return len(stk) == 0
            
            

