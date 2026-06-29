import operator

ops = {
    "+": operator.add,
    "*": operator.mul,
    "-": operator.sub,
    "/": operator.truediv,
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stk = []

        for token in tokens:
            if token in '+-*/':
                x = stk.pop()
                y = stk.pop()

                stk.append(ops[token](int(y), int(x)))
            else:
                stk.append(token)
        
        return int(stk[0])