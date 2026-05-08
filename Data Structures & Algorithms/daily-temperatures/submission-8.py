class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []

        for i, num in enumerate(temperatures):
            while stk and stk[-1][0] < num:
                temp, idx = stk.pop()
                res[idx] = i - idx
            stk.append([num, i])
        return res
            