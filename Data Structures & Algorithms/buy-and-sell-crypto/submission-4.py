class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        res = 0

        i = 0
        while i < len(prices)-1:
            j = i + 1

            if prices[i] > prices[j]:
                i = j
                continue

            while j < len(prices) and prices[i] < prices[j]:
                res = max(res, prices[j] - prices[i])
                j += 1 

            i = j
        
        return res
