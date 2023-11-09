#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
'''
# 就是写个生成斐波那契数列，我去
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]
'''
# f(n)只依赖于f(n-1)和f(n-2)，只需要两项就足够了\
# 只保留头两项，后面的全都不管了
class Solution:
    def climbStairs(self, n: int) -> int:
        a = b = 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
# @lc code=end

