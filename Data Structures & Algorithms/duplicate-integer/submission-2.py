class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length_nums = len(nums)
        nums = set(nums)
        return len(nums) != length_nums