class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        curSum = nums[0]
        maxSum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > curSum and curSum < 0:
                curSum = nums[i]
            else:
                curSum += nums[i]

            maxSum = max(maxSum, curSum)

        return maxSum
