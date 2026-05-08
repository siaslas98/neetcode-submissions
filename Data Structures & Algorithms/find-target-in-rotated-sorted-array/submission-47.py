class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r

            elif nums[l] > nums[mid] and nums[mid] < target <= nums[r]:
                l = mid + 1
            
            elif nums[l] > nums[mid] and target < nums[mid] < nums[l]:
                r = mid - 1
            
            else:
                l = mid + 1

        return l if 0 <= l < len(nums) and nums[l] == target else -1





