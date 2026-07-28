class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        stk = []



        for i in range(len(heights)):
            cur_height = heights[i]

            if not stk:
                stk.append(i)
                continue

            if cur_height > heights[stk[-1]]:
                stk.append(i)
                continue
            
            while stk and cur_height < heights[stk[-1]]:
                bar = stk.pop()
                prev_smaller = stk[-1] if stk else -1
                next_smaller = i

                width = next_smaller - prev_smaller - 1
                area = width * heights[bar]
                max_area = max(max_area, area)
            
            stk.append(i)

        
        while stk:
            bar = stk.pop()
            prev_smaller = stk[-1] if stk else -1

            width = n - prev_smaller - 1
            area = width * heights[bar]
            max_area = max(max_area, area)

        return max_area




