class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        for i in range(len(heights)):
            if not stk:
                stk.append(i)
                continue
            while stk and (heights[i] < heights[stk[-1]]):
                x = stk.pop()
                next_smaller = i
                prev_smaller = stk[-1] if stk else -1
                width = next_smaller - prev_smaller - 1
                max_area = max(max_area, width * heights[x])
            
            stk.append(i)

        while stk:
            x = stk.pop()
            next_smaller = len(heights)
            prev_smaller = stk[-1] if stk else -1
            width = next_smaller - prev_smaller - 1
            max_area = max(max_area, width * heights[x])

        return max_area


