class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        max_l, max_r = 0, len(height)-1

        area = 0

        while l < r:

            # update maximums
            if height[l] > height[max_l]:
                max_l = l
            if height[r] > height[max_r]:
                max_r = r

            # compute area to add for each index
            if height[l] <= height[r]:
                area += max(0, min(height[max_l], height[max_r]) - height[l])
                l += 1
            elif height[r] < height[l]:
                area += max(0, min(height[max_l], height[max_r]) - height[r])
                r -= 1
        
        return area