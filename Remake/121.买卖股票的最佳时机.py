#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
# 第n个位置表示在这天前哪天买入股票可以得到最大利润
# 记录下目前最小值所在的位置，并计算后面每一天与这个最小值的差值
# 当前一天的利润是前一天的最大可能与今天的最大的极大值
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0]*len(prices)
        minprice = prices[0]
        for i in range(0,len(prices)):
            minprice = min(minprice,prices[i])
            dp[i] = max(dp[i-1],prices[i]-minprice)
        return dp[i]
        

# @lc code=end

