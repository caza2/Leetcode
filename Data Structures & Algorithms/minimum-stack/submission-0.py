class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        check_min: int = self.stack.pop()
        if check_min == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]

        
