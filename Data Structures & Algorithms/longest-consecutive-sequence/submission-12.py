class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set()
        for num in nums:
            s.add(num)
        
        res = 1
        for i in range(len(nums)):
            s1 = 1
            n = nums[i]-1
            while n in s:
                s1 += 1
                s.remove(n)
                n -= 1
            n = nums[i] + 1
            while n in s:
                s1 += 1
                s.remove(n)
                n += 1
            res = max(res, s1)
        return res

