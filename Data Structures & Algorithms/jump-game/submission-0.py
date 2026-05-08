class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Ask the question, can you reach idx z from idx y, where 0 <= y <= z-1
        z = len(nums)-1

        while z > 0:
            y = z-1

            while y >= 0:
                if y + nums[y] >= z:
                    # True condition
                    z = y
                    break
                else:
                    y -= 1
            
            if z == 0:
                return True
            if y == -1:
                return False
        
        return True

            
            

                