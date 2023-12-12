#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#

# @lc code=start
'''
# 辅助栈法，先入后出，后入先出
# 前中括号就把之前的入栈，开始计算后面的
# 后中括号说明这一段结束，结算完后计算前一个中括号
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        mul = 0
        res = ""
        for i in s:
            if i == '[':
                stack.append([mul,res])
                mul = 0
                res = ""
            elif i == ']':
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif '0' <= i <= '9':
                mul = mul*10+int(i)
            else:
                res += i
        return res
'''
# DFS
# 以[作为递归开始的标志，]作为递归结束返回结果的标志
# i表示从第几位开始递归
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(s, i):
            mul = 0
            res = ""
            while i<len(s):
                if '0' <= s[i] <= '9':
                    mul = mul * 10 + int(s[i])
                elif s[i] == '[':
                    i, tmp = dfs(s, i + 1)
                    res += mul * tmp
                    mul = 0
                elif s[i] == ']':
                    return i, res
                else:
                    res += s[i]
                i += 1
            return res
        return dfs(s,0)


# @lc code=end

