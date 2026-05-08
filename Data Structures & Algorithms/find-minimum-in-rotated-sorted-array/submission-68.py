class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1
        res = 1001

        if nums[0] < nums[-1]:
            return nums[0]

        while low <= high:
            mid = low + (high - low) // 2

            if nums[low] < nums[mid]:
                res = min(res , nums[low])
                low = mid + 1
            elif nums[low] > nums[mid]:
                res = min(res, nums[mid])
                high = mid - 1
            else:
                res = min(res, nums[mid])
                res = min(res, nums[high])
                break
        return res
            


