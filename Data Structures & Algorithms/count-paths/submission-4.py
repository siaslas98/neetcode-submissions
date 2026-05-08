class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m * n == 1:
            return 1

        dp = [-1] * (m * n)

        dp[0] = 1
        
        for i in range(1, m*n):
            left, top = 0, 0 

            if i % n != 0:
                left = dp[i-1]

            if i // n != 0:
                top = dp[i-n]

            dp[i] = left + top
        
        return dp[-1]
