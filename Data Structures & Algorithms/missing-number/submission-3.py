class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) 
        total = n * (n + 1) // 2
        s = 0

        for num in nums:
            s += num
        
        return total - s