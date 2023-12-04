#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
'''
# 暴力解法，双循环直接检查
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(0,len(s)):
            for j in range(i, len(s)):
                t = s[i : j + 1]
                if t == t[::-1]:
                    res += 1
        return res
'''
'''
# 中心扩散法-双指针的基础上进行检查，最快
class Solution:
    def countSubstrings(self, s: str) -> int:
        def extend(s: str, i: int, j: int, n: int):
            res = 0
            while (i >= 0 and j < n and s[i] == s[j]):
                i -= 1
                j += 1
                res += 1
            return res
        res = 0
        for i in range(len(s)):
            res += extend(s, i, i, len(s))
            res += extend(s, i, i + 1, len(s))
        return res
'''
# DP解法，把第i个元素开始第j个结束的子串是否是回文串用二维DP列表记录
# 判断新子串是否是回文子串只需要在短一个字符的子串的基础上判断新增的两个字母即可
# 思路上兼具了双循环遍历和中心扩散法的核心思想
class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        res = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 1:
                        res += 1
                        dp[i][j] = True
                    elif dp[i + 1][j - 1]:
                        res += 1
                        dp[i][j] = True
        return res


# @lc code=end

