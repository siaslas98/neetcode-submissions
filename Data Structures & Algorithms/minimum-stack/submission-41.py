class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = None

    def push(self, val: int) -> None:
        if self.min_val is None:
            self.min_val = val
            self.min_stack.append(val)
        elif val < self.min_val:
            self.min_val = val
            self.min_stack.append(val)
        elif val == self.min_val:
            self.min_stack.append(val)
        self.stack.append(val)      

    def pop(self) -> None:
        top = self.stack.pop()

        if top is None: return

        if top == self.min_val:
            self.min_stack.pop()
            if self.min_stack:
                self.min_val = self.min_stack[-1]
            else:
                self.min_val = None

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_val
        
        
