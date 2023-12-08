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
# https://leetcode.cn/problems/regular-expression-matching/solutions/2361807/10-zheng-ze-biao-da-shi-pi-pei-dong-tai-m5z1i/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            dp[0][j] = dp[0][j - 2] and p[j - 1] == '*'
        # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]: dp[i][j] = True                              # 1.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]: dp[i][j] = True   # 2.
                    elif dp[i - 1][j] and p[j - 2] == '.': dp[i][j] = True        # 3.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]: dp[i][j] = True # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == '.': dp[i][j] = True    # 2.
        return dp[-1][-1]


# @lc code=end

