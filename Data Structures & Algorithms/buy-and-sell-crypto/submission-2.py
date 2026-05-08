class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l, r = 0, 1
        profit = 0

        while l < r and r < n:
            if prices[r] <= prices[l]:
                l = r
                r += 1
            elif prices[r] > prices[l]:
                profit = max(profit, prices[r]-prices[l])
                r += 1
        return profit
