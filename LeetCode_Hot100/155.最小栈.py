#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
'''
# 最常规的解法，但是非常慢
# 测试过复制列表以后排序，但是超时了，可能是复制要的时间太长
class MinStack:
    def __init__(self):
        self.items = [] 
    def push(self, val: int) -> None:
        self.items.append(val)  
    def pop(self) -> None:
        self.items.pop()
    def top(self) -> int:
        return self.items[len(self.items)-1]
    def getMin(self) -> int:
        min = self.top()
        for i in self.items:
            if min>i:
                min = i
        return min
'''
# 分析可知主要的复杂度优化应该在getmin函数上
# 尽量做到常数级的最小值查询
# 设置一个辅助栈，在元素加入的时候实时更新最小值
class MinStack:
    def __init__(self):
        self.items = [] 
        self.fitems = []
    def push(self, val: int) -> None:
        self.items.append(val)  
        if self.fitems == []:
            self.fitems.append(val)
        elif val <= self.fitems[-1]:
            self.fitems.append(val)
    def pop(self) -> None:
        if self.fitems == []:
            self.items.pop()
        else:
            if self.items.pop() == self.fitems[-1]:
                self.fitems.pop()
    def top(self) -> int:
        return self.items[len(self.items)-1]
    def getMin(self) -> int:
        return self.fitems[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

