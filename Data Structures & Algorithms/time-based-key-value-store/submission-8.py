class TimeMap:

    def __init__(self):
        self.map = {}


        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.map.get(key):
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]
        

    def get(self, key: str, timestamp: int) -> str:

        times = self.map.get(key)
        value = ""

        if times:

            left, right = 0, len(times) - 1

            while left <= right:
                mid = (left + right) // 2

                if times[mid][0] <= timestamp:
                    value = times[mid][1]
                    left = mid + 1
                else:
                    right = mid - 1
        
        return value



        
