#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
# 常规用栈的实现，match部分会造成多次判断
# 另外，必须要遍历完所有字符最后看栈是否为空，浪费时间
'''
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

def match(a,b):
    if (a == "(" and b == ")") or (a == "[" and b == "]") or (a == "{" and b == "}"):
        return True
    else:
        return False

class Solution:
    def isValid(self, s: str) -> bool:
        a = Stack()
        for i in s:
            if a.isEmpty():
                a.push(i)
            elif match(a.peek(),i):
                a.pop()
            else:
                a.push(i)
        return a.isEmpty()
'''           
# 基本上就是最优了，上面的都是靠运气刷时间数据了
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
    def isValid(self, s: str) -> bool:
        dic = {'{' :'}', '[':']','(':')'}
        a = Stack()
        # 应对"]"这样一上来不输入就要求读前面一个的数据
        for i in s:
            try:
                if i in dic:
                    a.push(i)
                elif (dic[a.pop()]!=i):
                    return False
            except IndexError as e:
                return False
        return a.isEmpty()
# @lc code=end

