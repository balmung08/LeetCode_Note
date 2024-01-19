#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        last = len(s)-1
        res = 0
        while s[last]!=" ":
            last-=1
            res+=1
            if last<0:
                return res
        return res
# @lc code=end

