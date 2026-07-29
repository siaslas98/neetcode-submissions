import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # To eat the bananas in each pile
        piles.sort()
        min_val = piles[-1]

        left, right = 1, piles[-1]

        while left <= right:
            mid = left + (right-left) // 2

            hours = 0
            for i in range(len(piles)):
                hours += math.ceil(piles[i] / mid)
                if hours > h:
                    break
            
            if hours > h:
                left = mid + 1
            
            if hours <= h:
                min_val = min(min_val, mid)
                right = mid - 1
        
        return min_val

            
