import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = high + 1

        while low <= high:
            x = 0
            mid = low + (high - low) // 2

            for num in piles:
                x += (num + mid - 1) // mid
                if x > h:
                    break
            if x <= h:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res