class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        prev_smaller = [-1] * len(heights)
        next_smaller = [len(heights)] * len(heights)
        stk = []

        def update_max(i):
            width = next_smaller[i] - prev_smaller[i] -1
            area = width * (heights[i])
            return max(area, max_area)


        for i in range(len(heights)):
            cur_height = heights[i]

            if not stk:
                stk.append(i)
                continue

            prev_height = heights[stk[-1]]
            if cur_height == prev_height:
                prev_smaller[i] = prev_smaller[stk[-1]]
                stk.append(i)
                continue

            if cur_height > prev_height:
                prev_smaller[i] = stk[-1]
                stk.append(i)
                continue
            
            while stk and cur_height < prev_height:
                next_smaller[stk[-1]] = i
                max_area = update_max(stk.pop())
                if stk:
                    prev_height = heights[stk[-1]]
            if stk:
                prev_smaller[i] = stk[-1]
            stk.append(i)
        
        while stk:
            max_area = update_max(stk.pop())
        
        return max_area




