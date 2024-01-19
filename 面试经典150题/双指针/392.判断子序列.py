#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target = 0
        point = 0
        while target<len(s) and point<len(t):
            if s[target] == t[point]:
                target+=1
                point+=1
            else:
                point+=1
        return target==len(s)
# @lc code=end

