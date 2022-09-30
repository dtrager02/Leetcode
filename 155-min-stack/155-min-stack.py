
class MinStack:
    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        min_val = self.getMin()
        if min_val == None or val < min_val:
            min_val = val
        self.data.append([val,min_val])


    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        return self.data[-1][0]

    def getMin(self) -> int:
        if not len(self.data):
            return None
        return self.data[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()