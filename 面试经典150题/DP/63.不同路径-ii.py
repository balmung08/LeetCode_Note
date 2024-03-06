#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#

# @lc code=start
# 其实不用单独拉出来第一行和第一列
# 因为一开始最后一行和最后一列初始值都是0
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        dp[0][0] = int(not obstacleGrid[0][0])
        for i in range(1,m):
            if obstacleGrid[i-1][0] == 0 and obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0
        for i in range(1,n):
            if obstacleGrid[0][i-1] == 0 and obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i-1]
            else:
                dp[0][i] = 0
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i-1][j] == 0:
                    dp[i][j] += dp[i-1][j]
                if obstacleGrid[i][j-1] == 0:
                    dp[i][j] += dp[i][j-1]
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
        return dp[-1][-1]

# @lc code=end

