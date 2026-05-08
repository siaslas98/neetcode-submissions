class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def addParen(op, close, s):
            if op == close == n:
                res.append(s)
            if op + 1 <= n:
                addParen(op + 1, close, s + "(")
            if close < op:
                addParen(op, close + 1, s + ")")
            
        addParen(0, 0, "")
        return res