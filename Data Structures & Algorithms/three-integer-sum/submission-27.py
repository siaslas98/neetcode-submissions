class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list
        # iterate through the list and fix at position i
        # target will be -nums[i]
        # perform 2 sum search from i+1 : len(nums)

        nums.sort()
        res = []

        for i in range(len(nums)):
            target = -nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1

            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif total < target:
                    l += 1
                elif total > target:
                    r -= 1
        
        return res
