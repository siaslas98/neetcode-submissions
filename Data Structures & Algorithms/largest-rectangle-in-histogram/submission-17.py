class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0

        for i in range(len(heights)):
            cur_height = heights[i]

            left, right = i-1, i+1

            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            
            width = right - left - 1
            area = width * (heights[i])
            max_area = max(area, max_area)
        
        return max_area




