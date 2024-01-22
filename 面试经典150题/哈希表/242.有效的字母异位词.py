#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
# 可以使用两个字典遍历并对比
# 也可以使用计数器进行计数
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i]+=1
            else:
                dic[i] = 1
        for key in dic:
            if dic[key] != t.count(key):
                return False
        return True
# @lc code=end

