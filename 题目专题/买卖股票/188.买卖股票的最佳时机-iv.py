#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
# 与问题三相同，仍旧可以使用增加维度或者增加状态两个思路实现
# 现在仅使用增加维度进行实现
# 买入时：DP[i][1][k]可能来自于DP[i-1][0][k]-price与DP[i-1][1][k]
# 卖出时：DP[i][0][0]可能来自DP[i-1][0][0]
# DP[i][0][k]可能来自DP[i-1][0][k]与DP[i-1][1][k-1]+price
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[[0]*(k+1) for i in range(2)] for j in range(n)]
        dp[0][0] = [0]*(k+1)
        dp[0][1] = [-prices[0]]*(k+1)
        for i in range(1,n):
            dp[i][0][0] = dp[i-1][0][0]
            for j in range(0,k):
                dp[i][1][j] = max(dp[i-1][0][j]-prices[i],dp[i-1][1][j])
            for j in range(1,k+1):
                dp[i][0][j] = max(dp[i-1][1][j-1]+prices[i],dp[i-1][0][j])
        return dp[-1][0][k]
    
# 2\n[3,3,5,0,0,3,1,4]
# @lc code=end

