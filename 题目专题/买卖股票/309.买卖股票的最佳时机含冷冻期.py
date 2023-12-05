#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 买卖股票的最佳时机含冷冻期
#

# @lc code=start
# 这一题也可以进行维度新增或者增加状态，本次选择状态新增进行实现
# 0为不持股，1为持股，2为冷冻期
# DP[i][0]可能来自于DP[i-1][0]与DP[i-1][2]
# DP[i][1]可能来自于DP[i-1][0]-price与DP[i-1][1]
# DP[i][2]可能来自于DP[i-1][1]+price与DP[i][0]
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[0 for i in range(3)] for j in range(n)]
        dp[0][0] = dp[0][2] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][2])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][1]+prices[i],dp[i][0])
        return dp[-1][2]
# @lc code=end

