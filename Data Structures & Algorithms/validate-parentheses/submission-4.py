class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        op = "([{"
        close = ")]}"

        for ch in s:
            if ch in op:
                stk.append(ch)
            else:
                if not stk: return False
                if ch == close[0] and stk[-1] == op[0]:
                    stk.pop()
                elif ch == close[1] and stk[-1] == op[1]:
                    stk.pop()
                elif ch == close[2] and stk[-1] == op[2]:
                    stk.pop()
                else:
                    return False

        return not stk