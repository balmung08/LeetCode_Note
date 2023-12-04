#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
'''
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]*(amount+1)
        for i in range(1,amount+1):
            flag = False
            dp[i] = i
            M = [n for n in coins if n<=dp[i]]
            if M==[]:
                dp[i] = -1
            else:
                for n in M:
                    if dp[i-n]+1<=dp[i] and dp[i-n]>=0:
                        flag = True
                        dp[i] = dp[i-n]+1
            if flag == False:
                dp[i] = -1
        return dp[-1]
'''
# 背包问题的经典模板
# 可以通过初始化设置来避免设置标志位
import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for n in [n for n in coins if n<=i]:
                if dp[i-n]+1<=dp[i]:
                    dp[i] = dp[i-n]+1
        return dp[-1] if(dp[-1] != math.inf) else -1
# @lc code=end
