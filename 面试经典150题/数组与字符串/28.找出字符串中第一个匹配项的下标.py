#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        end = len(needle)
        while end<=len(haystack):
            if haystack[start:end] == needle:
                return start
            else:
                start+=1
                end+=1
        return -1
# @lc code=end

