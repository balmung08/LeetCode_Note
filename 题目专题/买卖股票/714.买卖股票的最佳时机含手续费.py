#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
# 与122相同的思路，但是在状态转移的时候需要减去额外的成本
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)#列
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
# @lc code=end

