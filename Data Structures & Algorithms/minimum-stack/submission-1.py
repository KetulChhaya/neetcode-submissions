class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        min_ = min(val, self.min_stack[-1]) if self.min_stack else val
        self.min_stack.append(min_)
        return self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

        
