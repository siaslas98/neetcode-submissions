class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1, nums[0]]
        right = [1, nums[-1]]
        n = len(nums)

        for i in range(1, n):
            left.append(left[-1] * nums[i])

        print(left)
        
        for i in range(n-2, -1, -1):
            right.append(right[-1] * nums[i])
        
        print(right)


        res = [1] * (n + 1)

        for i in range(1, n+1):
            res[i] = left[i-1] * right[n-i]
        return res[1:]