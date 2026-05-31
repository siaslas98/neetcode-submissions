class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        i = 0

        while i < len(nums):
            target = nums[i]

            j, k = i + 1, len(nums)-1

            while j < k:
                total = nums[j] + nums[k]
                if total == -target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == nums[j-1]:
                        j +=1 
                    k -= 1
                    while k > -1 and nums[k] == nums[k + 1]:
                        k -= 1
                elif total < -target:
                    j += 1
                else:
                    k -= 1
            
            i += 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1

        return res
                





