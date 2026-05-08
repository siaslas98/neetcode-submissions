import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        low, high = 1, max(piles)-1
        x = 0
        res = max(piles)

        while low <= high:
            mid = low + (high - low) // 2

            for num in piles:
                x += math.ceil(num / mid)
                if x > h:
                    break
            
            if x <= h:
                res = min(res, mid)
                high = mid - 1
            else:
                low = mid + 1

            x = 0

        return res