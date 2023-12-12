'''
# python自带list实现
# 其实不满足题意
class CQueue:
    def __init__(self):
        self.List = []

    def appendTail(self, value: int) -> None:
        self.List.append(value)

    def deleteHead(self) -> int:
        if len(self.List):
            return self.List.pop(0)
        else:
            return -1
'''
# 双栈实现队列
# 加入就往b里放
# 需要输出时就把a的全部出栈再入栈到b中
# 此时a先入栈的在b里在栈顶，符合对列先入先出的特性
# 如果b没空就先把b出完，此时b里的每一个都比a先进队列
class CQueue:
    def __init__(self):
        self.List1 = []
        self.List2 = []
    def appendTail(self, value: int) -> None:
        self.List1.append(value)
    def deleteHead(self) -> int:
        if self.List2:
            return self.List2.pop()
        if not self.List1:
            return -1
        for i in range(0,len(self.List1)-1):
            self.List2.append(self.List1.pop()) 
        return self.List1.pop()
# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()