class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def findMin(nums: List[int]) -> int:
            low, high = 0, len(nums)-1
            res = 0

            if nums[0] <= nums[-1]:
                return 0

            while low <= high:
                mid = low + (high - low) // 2

                if nums[low] < nums[mid]:
                    res = low
                    low = mid + 1
                elif nums[low] > nums[mid]:
                    res = mid
                    high = mid - 1
                else:
                    if nums[mid] < nums[res]:
                        res = mid
                    if nums[high] < nums[res]:
                        res = high
                    break
            return res
        
        def findTarget(low: int, high: int, nums: List[int], target: int) -> int:

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    low = mid + 1
                elif nums[mid] > target:
                    high = mid - 1

            return -1 


        
        min_idx = findMin(nums)
        resLeft = findTarget(0, min_idx, nums, target)
        resRight = findTarget(min_idx, len(nums)-1, nums, target)

        if resLeft != -1:
            return resLeft
        if resRight != -1:
            return resRight
        
        return -1
        


                