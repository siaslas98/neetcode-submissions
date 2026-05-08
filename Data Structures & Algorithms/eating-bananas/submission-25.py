class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # When k is >= piles[i] we can finish the ith pile in 1 hour
        # When k < piles[i] it will take us piles[i] // k + piles[i] % 2 number of hours to finish the ith pile.
        # What do we initialize k to?
        # Remember, we are trying to minimize k.
        # Pick the mid point value for k.
        # If middle value leads to the eating completing in h hours, then try to reduce it.
        # Else increase it.

        max_val = max(piles)
        l = 1
        res, r = max_val, max_val

        while l <= r:
            k = l + (r-l) // 2 # mid == k 
            x = h

            for idx, pile in enumerate(piles):
                if piles[idx] <= k:
                    x -= 1
                else:
                    x -= math.ceil(piles[idx] / k)

                if x < 0:
                    l = k + 1 # This k value is too small
                    break

                if idx == (len(piles) - 1) and x >= 0:
                    res = min(res, k)
            
            if x >= 0:
                r = k - 1

        return res


