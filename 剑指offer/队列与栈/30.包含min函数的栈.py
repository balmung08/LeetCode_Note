class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.List = []
        self.List_m = []

    def push(self, x: int) -> None:
        self.List.append(x)
        if not self.List_m or x<=self.List_m[-1]:
            self.List_m.append(x)

    def pop(self) -> None:
        if self.List.pop()==self.List_m[-1]:
            self.List_m.pop()

    def top(self) -> int:
        return self.List[-1]

    def getMin(self) -> int:
        return self.List_m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()