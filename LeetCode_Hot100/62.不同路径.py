#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
# 二维DP
# 要初始化的不仅是01和10两格，而是01和10的一行一列，他们都是初始情况
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
# @lc code=end

