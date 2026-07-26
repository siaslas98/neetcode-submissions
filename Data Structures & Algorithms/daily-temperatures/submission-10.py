class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        res = [0] * len(temperatures)
        stk = [0]

        for i in range(1, len(temperatures)):
            
            while stk and temperatures[i] > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            
            stk.append(i)
        
        return res
