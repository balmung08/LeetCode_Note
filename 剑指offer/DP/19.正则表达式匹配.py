#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#

# @lc code=start
'''
# 建两个指针，一起迭代来依次判断是否相等
# 没有考虑a*可以重复0次或者n次的情况，仅认为其可以重复一次
# 要考虑的话需要很复杂的标志位和边界条件判断，非常丑陋
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        arrow = 0
        dp = [False]*(n)
        s_pre = None
        for i in range(0,n):
            if i<m and p[arrow]!='*' and p[arrow]!='.':
                if s[i] == p[arrow]:
                    dp[i] = True
                    arrow += 1
                    s_pre = p[i]
                else:
                    dp[i] = False
                    arrow += 1
                    s_pre = s[i]
            elif i<m and p[arrow]=='.':
                dp[i] = True
                arrow += 1
                s_pre = p[i]
            elif i<m and p[arrow]=='*':
                if s[i] == s_pre or s_pre == ".":
                    dp[i] = True
                elif s[i] != s_pre:
                    arrow += 1
        return dp
# "aaaa"\n"a*"\n
'''
# 常规的DP思路
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def match(charS: str, charP: str) -> bool:
            return charP == '.' or charP == charS

        lenS, lenP = len(s), len(p)
        dp = [[False] * (lenS+1) for _ in range(lenP+1)]
        dp[0][0] = True

        for i in range(1, lenP+1):
            if p[i-1] == '*':
                dp[i][0] = dp[i-2][0]
        for i in range(1, lenP+1):
            for j in range(1, lenS+1):
                if p[i-1] == '*':
                    if match(s[j-1], p[i-2]):
                        dp[i][j] = dp[i-2][j] or dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-2][j]
                else:
                    dp[i][j] = match(s[j-1], p[i-1]) and dp[i-1][j-1]
        
        return dp[-1][-1]
# @lc code=end

