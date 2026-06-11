class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0
        
        res = 0
        nextL = [None] * len(height)

        # Idea is that if we know prev largest and next largest, we can calculate the area contrinution by index i.

        # Build next largest info.
        for i in range(len(height)-2, -1, -1):
            if nextL[i+1] == None and height[i+1] > height[i]:
                nextL[i] = i+1
            elif nextL[i+1] != None and height[nextL[i+1]] > height[i]:
                nextL[i] = nextL[i+1]

        prevL = 0
        i = 1
        while i < len(height)-1:

            if height[prevL] < height[i]:
                prevL = i
                i += 1
                continue
        
            if nextL[i] == None:
                i += 1
                continue
            
            res += min(height[prevL], height[nextL[i]]) - height[i]

            i += 1
        
        return res
            

            



