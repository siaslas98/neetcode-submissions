import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1 and tokens[0].isdigit():
            return int(tokens[0])

        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }

        stk = []
        res = 0
        
        for i in range(len(tokens)):
            if tokens[i] not in ops:
                stk.append(int(tokens[i]))
            else:
                op = tokens[i]
                res = ops[op](stk[-2], stk[-1])
                stk.pop()
                stk.pop()
                stk.append(int(res))
        
        return int(res)

            

        
            










