class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1

            comp = nums[i] * -1

            while l < r:
                if nums[l] + nums[r] == comp:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and l > 0 and r < len(nums)-1 and nums[l] == nums[l-1] and nums[r] == nums[r+1]:
                        l += 1
                        r -= 1
                elif nums[l] + nums[r] > comp:
                    r -= 1
                    while r > 0 and nums[r] == nums[r+1]:
                        r -= 1
                elif nums[l] + nums[r] < comp:
                    l += 1
                    while nums[l] == nums[l-1]:
                        l += 1
        return res