class MinStack:

    def __init__(self):
        self.arr = []
        self.min_val = math.inf

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.arr.append(val)
        
    def pop(self) -> None:
        self.arr.pop()
        self.min_val = math.inf
        for num in self.arr:
            self.min_val = min(self.min_val, num)
        
    def top(self) -> int:
        return self.arr[-1] if self.arr else None
        
    def getMin(self) -> int:
        return self.min_val

        
