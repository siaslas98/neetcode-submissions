class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        l = 1
        res, r = max_val, max_val

        while l <= r:
            k = l + (r-l) // 2 # mid == k 
            x = h

            for pile in piles:
                if pile <= k:
                    x -= 1
                else:
                    x -= math.ceil(pile / k)

                if x < 0:
                    l = k + 1 # This k value is too small
                    break
            
            if x >= 0:
                res = min(res, k)
                r = k - 1

        return res


