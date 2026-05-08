class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def findSum(comb, curSum, start):
            if curSum == target:
                res.append(comb[:])
            
            for i in range(start, len(nums)):
                num = nums[i]
                if curSum + num > target:
                    continue
                comb.append(num)
                findSum(comb, curSum + num, i)
                comb.pop()

        findSum([], 0, 0)
        return res