class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def build(subset, start, nums):
            nonlocal res
            res.append(subset[:])

            for i in range(start, len(nums)):
                subset.append(nums[i])
                build(subset, i+1, nums)
                subset.pop()
        
        build([], 0, nums)
        return res
