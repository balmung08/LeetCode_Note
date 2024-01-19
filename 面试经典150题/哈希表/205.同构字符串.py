#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#

# @lc code=start
'''
# 映射要互相一对一，如果只用一个哈希表没法检查
# 用两个检查是否有多对一和一对多
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic1=dict()
        dic2=dict()
        for i in range(len(s)):
            if (s[i] in dic1 and dic1[s[i]]!=t[i]) or (t[i] in dic2 and dic2[t[i]]!=s[i]):
                return False
            dic1[s[i]]=t[i]
            dic2[t[i]]=s[i]
        return True
'''
# 用index函数检查每个元素和其映射在两个字符串里出现的位置是否相同
# index是返回第一次出现的索引，而一个确定的字符其第一次出现的索引是固定性质
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        for i in range(len(s)):
            if s.index(s[i]) != t.index(t[i]):
                return False
        return True 

# @lc code=end

