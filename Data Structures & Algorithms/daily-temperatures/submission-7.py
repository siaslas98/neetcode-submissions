class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stk = []

        for i, num in enumerate(temperatures):
            while stk and stk[-1][0] < num:
                temp, idx = stk.pop()
                res[idx] = i - idx
            stk.append([num, i])
        return res
            