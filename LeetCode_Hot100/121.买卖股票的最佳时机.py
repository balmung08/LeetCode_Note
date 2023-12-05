#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
'''
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
'''
# 上面那个其实是维护最小值，不算是动态规划的思路，下面按照通用思路完成
# 使用DP[0][0]和DP[0][1]来表示第1天未买入和已买入的情况，内容就是手里持有的金额
# 股票问题的通用递推公式：
# 买入时：DP[i][1]可能来自于-price(买入)与DP[i-1][1](保持)
# 卖出时：DP[i][0]可能来自DP[i-1][0](保持)与DP[i-1][1]+price(卖出)
# 保持每天的利润最大化，因此每天都得比较并保持最大值
# 这题由于只能买卖一次，故在买股票以前手里是没钱的
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)#列
        dp = [[0 for i in range(2)] for j in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]
# @lc code=end

