class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        prev_smaller = [-1] * len(heights)
        next_smaller = [len(heights)] * len(heights)
        stk = []

        for i in range(len(heights)-1, -1, -1):
            if not stk:
                stk.append(i)
                continue
            
            while stk and heights[i] < heights[stk[-1]]:
                prev_smaller[stk[-1]] = i
                stk.pop()
            stk.append(i)

        for i in range(len(heights)):
            if not stk:
                stk.append(i)
                continue
            while stk and heights[stk[-1]] > heights[i]:
                next_smaller[stk[-1]] = i
                stk.pop()
            stk.append(i)

        for i in range(len(heights)):
            cur_height = heights[i]

            width = next_smaller[i] - prev_smaller[i] - 1
            area = width * (heights[i])
            max_area = max(area, max_area)
        
        return max_area




