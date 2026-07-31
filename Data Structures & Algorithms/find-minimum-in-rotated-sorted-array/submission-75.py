class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1


        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2

            if nums[left] < nums[mid]:
                left = mid
                continue
            if nums[left] > nums[mid]:
                right = mid
                continue
            if nums[left] == nums[mid]:
                return nums[left+1]
        
        return nums[left]

            