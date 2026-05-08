class Solution:

    def climbStairs(self, n: int) -> int:
        res = 0
        
        def climb(val):
            nonlocal res
            nonlocal n

            if val == n:
                res += 1
            if val > n:
                return
            
            climb(val+1)
            climb(val+2)
        
        climb(0)
        return res
