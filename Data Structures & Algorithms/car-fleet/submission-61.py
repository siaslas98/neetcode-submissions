import math 

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = [(position[i], speed[i]) for i in range(n)]
        sorted_cars = sorted(cars, key=lambda item: item[0])
        max_steps = None
        res = 0

        for i in range(n-1, -1, -1):       
            pos, speed = sorted_cars[i] 

            if max_steps is None:
                max_steps = (target - pos) / speed
            else:
                steps = (target - pos) / speed
                if steps > max_steps:
                    res += 1
                    max_steps = steps
        
        res += 1
        return res



