#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)#行
        n = len(grid[0])#列
        dp = [[0 for i in range(n)] for j in range(m)]
        res = 0
        for i in range(m):
            res += grid[i][0]
            dp[i][0] = res
        res = 0
        for i in range(n):
            res += grid[0][i]
            dp[0][i] = res
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[-1][-1]


# @lc code=end

