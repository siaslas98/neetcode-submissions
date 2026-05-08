class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        used = set()

        def findSum(comb, curSum):
            if curSum == target:
                res.append(comb[:])
            
            for num in nums:
                if curSum + num > target:
                    continue
                comb.append(num)
                findSum(comb, curSum + num)
                comb.pop()
        
        findSum([], 0)
        unique = {tuple(sorted(sub)) for sub in res}
        return [list(t) for t in unique]