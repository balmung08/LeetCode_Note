#
# @lc app=leetcode.cn id=123 lang=python3
#
# [123] 买卖股票的最佳时机 III
#

# @lc code=start
# 可以增加状态或者增加维度
'''
# ①在状态维度里增加不同状态
# 01234分别表示交易的次数
# 买入时：DP[i][1]可能来自于DP[i-1][0]-price与DP[i-1][1]
# DP[i][3]可能来自于DP[i-1][2]-price与DP[i-1][3]
# 卖出时：DP[i][0]可能来自DP[i-1][0]
# DP[i][2]可能来自DP[i-1][2]与DP[i-1][1]+price
# DP[i][4]可能来自DP[i-1][4]与DP[i-1][3]+price
# 同一天可以多次买卖
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[0 for i in range(5)] for j in range(n)]
        dp[0][0] = dp[0][2]  = dp[0][4] = 0
        dp[0][1] = -prices[0]
        dp[0][3] = -prices[0]
        for i in range(1,n):
            dp[i][0] = dp[i-1][0]
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2] = max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3] = max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4] = max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[-1][-1]
'''
# 在持股维度以外新增买卖次数状态维度
# 第三维度表示卖出的次数，共有0 1 2三种情况
# 买入时：DP[i][1][0]可能来自于DP[i-1][0][0]-price与DP[i-1][1][0]
# DP[i][1][1]可能来自于DP[i-1][0][1]-price与DP[i-1][1][1]
# 卖出时：DP[i][0][0]可能来自DP[i-1][0][0]
# DP[i][0][1]可能来自DP[i-1][0][1]与DP[i-1][1][0]+price
# DP[i][0][2]可能来自DP[i-1][0][2]与DP[i-1][1][1]+price
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[[0,0,0] for i in range(2)] for j in range(n)]
        dp[0][0][0] = dp[0][0][1] = dp[0][0][2] = 0
        dp[0][1][0] = dp[0][1][1] = -prices[0]
        for i in range(1,n):
            dp[i][0][0] = dp[i-1][0][0]
            dp[i][0][1] = max(dp[i-1][0][1],dp[i-1][1][0]+prices[i])
            dp[i][1][0] = max(dp[i-1][1][0],dp[i-1][0][0]-prices[i])
            dp[i][1][1] = max(dp[i-1][1][1],dp[i-1][0][1]-prices[i])
            dp[i][0][2] = max(dp[i-1][0][2],dp[i-1][1][1]+prices[i])
        return dp[-1][0][2]
# @lc code=end

