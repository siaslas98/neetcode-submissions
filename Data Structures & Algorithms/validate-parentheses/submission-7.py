class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stk = []

        for ch in s:
            if ch in "([{":
                stk.append(ch)
            else:
                if not stk:
                    return False
                if ch == ")" and stk[-1] != "(":
                    return False
                elif ch == "]" and stk[-1] != "[":
                    return False
                elif ch == "}" and stk[-1] != "{":
                    return False
                
                stk.pop()
                
        
        return len(stk) == 0 
