class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # determine whether to start at index 0 or 1
        if len(cost) == 2:
            return min(cost[0], cost[1])
        
        if len(cost) == 3:
            return min(cost[0] + cost[1], cost[0] + cost[2], cost[1])

        
        A = min(cost[0] + cost[1], cost[0] + cost[2])
        B = min(cost[1] + cost[2], cost[1] + cost[3])

        i = 0 if A < B else 1
        res = cost[i]

        while i < len(cost):
            if i + 2 < len(cost):
                if cost[i] + cost[i+2] <= cost[i] + cost[i+1]:
                    i += 2
                else:
                    i += 1
                res += cost[i]
                continue
            i += 1

        return res



    
