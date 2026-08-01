class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if left == mid and nums[right] == target:
                return right
            
            if nums[left] < nums[right]:
                if target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[left] < nums[mid] and target < nums[left]:
                left = mid + 1
            
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif nums[right] < nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1        

        return -1