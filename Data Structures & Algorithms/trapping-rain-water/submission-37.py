class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        

        l, r = 0, len(height)-1
        leftM, rightM = height[l], height[r]
        res = 0

        while l < r:
            if leftM < rightM:
                l += 1
                leftM = max(leftM, height[l])
                res += leftM - height[l]
            else:
                r -= 1
                rightM = max(rightM, height[r])
                res += rightM - height[r]
        
        return res


        