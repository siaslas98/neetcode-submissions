class TimeMap:

    def __init__(self):
        self.mp = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mp:
            self.mp[key].append([timestamp, value])
        else:
            self.mp[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.mp.get(key, "")
        if not arr:
            return arr

        # [[1, "happy"] [2, "good"], [3, "wind"]]

        l = 0
        r = len(arr)-1

        val = ""
        while l <= r:
            mid = (l+r)//2
            if arr[mid][0] > timestamp:
                r = mid - 1
            elif arr[mid][0] < timestamp:
                val = arr[mid][1]
                l = mid + 1
            else:
                return arr[mid][1]

        return val


        
        
