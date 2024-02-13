#
# @lc app=leetcode.cn id=71 lang=python3
#
# [71] 简化路径
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['/']
        path = path.split('/')
        path = list(filter(None, path))
        res = ""
        for i in path:
            if i=='.':
                pass
            elif i=='..':
                if len(stack)!=1:
                    stack.pop()
            else:
                stack.append(i)
        for i in range(len(stack)):
            if stack[i]!='/' and stack[i-1]!='/':
                res+='/'
            res+=stack[i]
        return res
# 对stack的输出结构进行简化
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")
        res = ""
        for i in path:
            if i=='.':
                pass
            elif i=='..':
                if stack:
                    stack.pop()
            elif i:
                stack.append(i)
        return "/"+"/".join(stack)
# @lc code=end

