#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#

# @lc code=start
'''
# 暴力法果然超时了
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        for i in range(0,len(temperatures)):
            for j in range(i+1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = (j-i)
                    break
        return result
'''
'''
# 必须在一个循环里完成
# 用栈存储下标，i因为n弹出的话返回值就是i-n
# 非常慢，把栈的功能提取出来试试
class Stack: 
    def __init__(self): 
        self.items = []  
    def isEmpty(self): 
        return self.items == []  
    def push(self, item): 
        self.items.append(item)  
    def pop(self): 
        return self.items.pop()  
    def peek(self): 
        return self.items[len(self.items)-1]   

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = Stack()
        result = [0]*len(temperatures)
        temp = []
        for index,value in enumerate(temperatures):
            while not s.isEmpty() and value>temperatures[s.peek()]:
                result[s.pop()] = index - s.peek()
            s.push(index)
        return result
'''   
# 把栈的功能直接写出来，因为调用函数需要花费额外的时间
# 这样逻辑和上面完全一致但省下了很多时间
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        result = [0]*len(temperatures)
        temp = []
        for index,value in enumerate(temperatures):
            while s and value>temperatures[s[-1]]:
                result[s.pop()] = index - s[-1]
            s.append(index)
        return result


# @lc code=end

