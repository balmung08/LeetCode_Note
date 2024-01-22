#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#

# @lc code=start
'''
# 完全使用指针和双哈希表实现
# 有很多条件判断
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic1=dict()
        dic2=dict()
        start = 0
        old = 0
        for i in range(len(pattern)):
            while s[start]!=" ":
                start+=1
                if start==len(s):
                    break
            if (pattern[i] in dic1 and dic1[pattern[i]]!=s[old:start]) or (s[old:start] in dic2 and dic2[s[old:start]]!=pattern[i]):
                return False
            dic1[pattern[i]]=s[old:start]
            dic2[s[old:start]]=pattern[i]
            if start == len(s):
                if i != len(pattern)-1:
                    return False
                break
            start+=1
            old = start
        return start==len(s) 
'''
# 首先用split拆掉后判断长度，可以省去很多判断
# 拆成单词以后和205一模一样的思路
class Solution:
    def wordPattern(self, pattern, s):
        s = s.split()
        if len(pattern) != len(s):
            return False
        x = {}
        y = {}
        for i in range(len(pattern)):
            if (pattern[i] in x and x[pattern[i]] != s[i]) or (s[i] in y and y[s[i]] != pattern[i]):
                return False
            x[pattern[i]] = s[i]
            y[s[i]] = pattern[i]
        return True

# @lc code=end

