#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
# 与121的唯一区别在于买时之前可以买卖过，初始金额不一定为0了
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]

# @lc code=end

